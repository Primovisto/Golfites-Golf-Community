from django.contrib import messages, auth
from accounts.forms import UserLoginForm
from django. urls import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from ads.models import Ad
from golfer.models import GolferProfile


# Create your views here.
def index(request):
    latest_ads = Ad.objects.all().order_by('-id')[:2]
    golfers = GolferProfile.objects.all().order_by('-id')[:8]
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

    args = {'form': form, 'latest_ads': latest_ads, 'golfers': golfers}
    args.update(csrf(request))
    return render(request, 'index.html', args)
