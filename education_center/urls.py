from django.conf.urls import url
from education_center import views

urlpatterns = [
    url(r'^$', views.education_post_list, name='education_blog'),
    url(r'^(?P<id>\d+)/$', views.education_post_detail, name='education_blog_post'),
    url(r'^education_center/top', views.education_top_posts),
    url(r'^post/new/$', views.education_new_post, name='education_new_post'),
    url(r'^education_center/(?P<id>\d+)/edit$', views.education_edit_post, name='education_edit'),
]