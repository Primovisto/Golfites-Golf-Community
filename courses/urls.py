from django.conf.urls import url

from courses import views
from courses.views import search_names, course_page

urlpatterns = [
    url(r'^$', views.courses, name='courses'),
    url(r'^(?P<id>\d+)/$', course_page, name='coursepage'),
    url(r'^courses/search/$', search_names, name='search'),


]
