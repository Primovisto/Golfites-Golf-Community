from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponseRedirect
from .models import Ad
from .forms import NewAdForm
from django.contrib.auth.decorators import login_required


def all_ads(request):
    ads = Ad.objects.all()
    return render(request, "ads/ads.html", {"ads": ads})


def ads_page(request, id):
    ad = get_object_or_404(Ad, pk=id)
    ad.views += 1
    ad.save()
    return render(request, "ads/adspage.html", {"ad": ad})


@login_required(login_url="/accounts/login?next=ads/new/")
def add_new_ad(request):
    if request.method == "POST":
        form = NewAdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.advertiser = request.user
            ad.save()
            return redirect(ads_page, ad.pk)
    else:
        form = NewAdForm()
    return render(request, 'ads/newadform.html', {'form': form})


@login_required(login_url="/accounts/login?next=ads/edit/")
def edit_ad(request, id):
    ad = get_object_or_404(Ad, pk=id)
    if request.method == "POST":
        form = NewAdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.advertiser = request.user
            ad.save()

            return redirect(ads_page, ad.pk)
    else:
        form = NewAdForm(instance=ad)
    return render(request, 'ads/newadform.html', {'form': form})


@login_required(login_url="/accounts/login?next=ads/delete/")
def delete_ad(request, id):
    ad = Ad.objects.filter(pk=id)
    ad.delete()
    return HttpResponseRedirect(reverse('ads'))
