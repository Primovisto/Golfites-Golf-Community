from django.conf.urls import url
from .views import register, login, profile, logout, change_password

urlpatterns = [
    url(r'^register', register, name='register'),
    url(r'^login', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^profile', profile, name='profile'),
    url(r'^change_password/$', change_password, name='change_password'),

    ]
