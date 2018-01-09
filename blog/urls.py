from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.post_list, name='blog'),
    url(r'^(?P<id>\d+)/$', views.post_detail, name='blog_post'),
    url(r'^blog/top', views.top_posts),
    url(r'^post/new/$', views.new_post, name='new_post'),
    url(r'^blog/(?P<id>\d+)/edit$', views.edit_post, name='edit'),
    url(r'^$', views.all_bloggers, name='all_bloggers'),
]
