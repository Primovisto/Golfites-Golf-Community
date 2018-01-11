from django.shortcuts import render, get_object_or_404
from .models import GolferProfile


def all_golfers(request):
    golfers = GolferProfile.objects.all()
    return render(request, "golfers/golfers.html", {"golfers": golfers})


def golfer_page(request, id):
    golfers = get_object_or_404(GolferProfile, pk=id)
    golfers.save()
    return render(request, "golfers/golferprofile.html", {"golfers": golfers})
