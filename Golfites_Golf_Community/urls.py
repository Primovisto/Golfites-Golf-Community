"""Golfites_Golf_Community URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.views.static import serve
from Golfites_Golf_Community.settings import MEDIA_ROOT
from accounts import urls as accounts_urls
from blog import urls as blog_urls
from equipment import urls as equipment_urls
from golfer import urls as golfers_urls
from education_center import urls as education_center_urls
from threads import urls as threads_urls
from ads import urls as ads_urls
from home.views import index
from courses import urls as courses_urls


urlpatterns = [
    url(r'^accounts/', include(accounts_urls)),
    url(r'^equipment/', include(equipment_urls)),
    url(r'^blog/', include(blog_urls)),
    path('admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^forum/', include(threads_urls)),
    url(r'^education_center/', include(education_center_urls)),
    url(r'^courses/', include(courses_urls)),
    url(r'^golfers/', include(golfers_urls)),
    url(r'^ads/', include(ads_urls)),

]
