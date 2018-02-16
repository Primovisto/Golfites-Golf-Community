from django.shortcuts import render, get_object_or_404, redirect
from .models import GolferProfile
from .forms import NewGolferForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login?next=golfers/')
def all_golfers(request):
    golfers = GolferProfile.objects.all()
    return render(request, "golfers/golfers.html", {"golfers": golfers})


@login_required(login_url='/accounts/login?next=golfers/(?P<id>\d+)/')
def golfer_page(request, id):
    golfer = get_object_or_404(GolferProfile, pk=id)
    golfer.save()
    return render(request, "golfers/golferprofile.html", {"golfer": golfer})


@login_required(login_url="/accounts/login?next=golfers/new/")
def add_new_golfer(request):
    if request.method == "POST":
        form = NewGolferForm(request.POST, request.FILES)
        if form.is_valid():
            golfer = form.save(commit=False)
            golfer.golfer = request.user
            golfer.save()
            return redirect(golfer_page, golfer.pk)
    else:
        form = NewGolferForm()
    return render(request, 'golfers/creategolferform.html', {'form': form})


@login_required
def edit_golfer(request, id):
    golfer = get_object_or_404(GolferProfile, pk=id)
    if request.method == "POST":
        form = NewGolferForm(request.POST, request.FILES, instance=golfer)
        if form.is_valid():
            golfer = form.save(commit=False)
            golfer.golfer = request.user
            golfer.save()

            return redirect(golfer_page, golfer.pk)
    else:
        form = NewGolferForm(instance=golfer)
    return render(request, 'golfers/creategolferform.html', {'form': form})
