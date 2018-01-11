
from django.conf.urls import url
from .views import all_golfers, golfer_page, add_new_golfer, edit_golfer

urlpatterns = [

    url(r'^$', all_golfers, name='all_golfers'),
    url(r'^(?P<id>\d+)/$', golfer_page, name='golfer_page'),
    url(r'^new/$', add_new_golfer, name='new'),
    url(r'^(?P<id>\d+)/edit/$', edit_golfer, name='editgolfer'),

]
