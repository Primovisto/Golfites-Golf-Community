from django.shortcuts import render
from courses.models import Course


# Create your views here.
def courses(request):
    all_courses = Course.objects.all().order_by('name')
    return render(request, 'courses/course-map.html', {'all_courses': all_courses})
