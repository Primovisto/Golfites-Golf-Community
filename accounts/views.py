from django.contrib import messages, auth
from accounts.forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.forms import PasswordChangeForm
from django. urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import csrf
from golfer.models import GolferProfile
from ads.models import Ad
from ads.views import ads_page
from django.conf import settings
from ads.forms import NewAdForm
import datetime
import stripe

stripe.api_key = settings.STRIPE_SECRET


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount=999,
                    currency="USD",
                    description=form.cleaned_data['email'],
                    card=form.cleaned_data['stripe_id'],
                )
                if customer.paid:
                    form.save()
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


def profile(request):
    golfers = GolferProfile.objects.all()
    ads = Ad.objects.all()
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
