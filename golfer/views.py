from django.shortcuts import render, get_object_or_404
from .models import GolferProfile


def all_golfers(request):
    golfers = GolferProfile.objects.all()
    return render(request, "golfers/golfers.html", {"golfers": golfers})


def golfer_page(request, id):
    golfer = get_object_or_404(GolferProfile, pk=id)
    golfer.save()
    return render(request, "golfers/golferprofile.html", {"golfer": golfer})
