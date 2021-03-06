from django.contrib import messages, auth
from accounts.forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django. urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import csrf
from golfer.models import GolferProfile
from ads.models import Ad
from ads.views import ads_page
from django.conf import settings
from ads.forms import NewAdForm
import arrow
import datetime
import stripe
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from accounts.models import User
from django.views.decorators.csrf import ensure_csrf_cookie


stripe.api_key = settings.STRIPE_SECRET


@ensure_csrf_cookie
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                customer = stripe.Customer.create(
                    email=form.cleaned_data['email'],
                    card=form.cleaned_data['stripe_id'],  # this is currently the card token/id
                    plan='GOLFITES_SUB',
                )

                if customer:
                    user = form.save()
                    user.stripe_id = customer.id
                    user.subscription_end = arrow.now().replace(weeks=+4).datetime
                    user.save()
                    user = auth.authenticate(email=request.POST.get('email'),
                                             password=request.POST.get('password1'))

                    if user:
                        auth.login(request, user)
                        messages.success(request, "You have successfully registered")
                        return redirect(reverse('profile'))
                    else:
                        messages.error(request, "unable to log you in at this time!")
                else:
                    messages.error(request, "We were unable to take a payment with that card!")
            except stripe.error.CardError as e:
                messages.error(request, "Your card was declined!")
    else:
        today = datetime.date.today()
        form = UserRegistrationForm()

    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE}
    args.update(csrf(request))

    return render(request, 'register.html', args)


@login_required(login_url='/login?next=profile')
def profile(request):
    golfers = GolferProfile.objects.all()
    ads = Ad.objects.all().order_by('-published_date')
    args = {'ads': ads, 'golfers': golfers}
    args.update(csrf(request))
    return render(request, 'profile.html', args)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your email or password was not recognised")

    else:
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'login.html', args)


def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            return render(request, 'password_change_message.html')

    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'change_password.html', args)


def edit_ad(request, id):
    ad = get_object_or_404(Ad, pk=id)
    if request.method == "POST":
        form = NewAdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.seller = request.user
            ad.save()

            return redirect(ads_page, ad.pk)
    else:
        form = NewAdForm(instance=ad)
    return render(request, 'ads/newadform.html', {'form': form})


@login_required(login_url='/accounts/login/')
def cancel_subscription(request):
    try:
        customer = stripe.Customer.retrieve(request.user.stripe_id)
        customer.cancel_subscription(at_period_end=True)
    except Exception as e:
        messages.error(request, e)
    return redirect('profile')


@csrf_exempt
def subscriptions_webhook(request):
    event_json = json.loads(request.body)
    # Verify the event by fetching it from Stripe
    try:
        # firstly verify this is a real event generated by Stripe.com
        # commented out for testing - uncomment when live
        # event = stripe.Event.retrieve(event_json['object']['id'])
        cust = event_json['object']['customer']
        paid = event_json['object']['paid']
        user = User.objects.get(stripe_id=cust)
        if user and paid:
            user.subscription_end = arrow.now().replace(weeks=+4).datetime  # 4 weeks from now
            user.save()

    except stripe.InvalidRequestError as e:
        return HttpResponse(status=404)
    return HttpResponse(status=200)
