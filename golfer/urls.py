
from django.conf.urls import url
from .views import all_golfers, golfer_page

urlpatterns = [

    url(r'^$', all_golfers, name='all_golfers'),
    url(r'^(?P<id>\d+)/$', golfer_page, name='golfer_page'),

]