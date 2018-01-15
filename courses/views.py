from django.shortcuts import render, render_to_response, get_object_or_404
from courses.models import Course


# Create your views here.
def courses(request):
    all_courses = Course.objects.all().order_by('name')
    return render(request, 'courses/course-map.html', {'all_courses': all_courses})


def course_page(request, id):
    courses = get_object_or_404(Course, pk=id)
    courses.save()
    return render(request, "courses/course-page.html", {"courses": courses})


def search_names(request):
    if request.method == "POST":
        search_text = request.POST['search_text']

    else:
        search_text = ''

    courses = Course.objects.filter(name__contains=search_text)

    return render_to_response('ajax_search.html', {'courses': courses})


