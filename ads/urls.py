from django.conf.urls import url
from .views import all_ads, ads_page, add_new_ad

urlpatterns = [

    url(r'^$', all_ads, name='ads'),
    url(r'^(?P<id>\d+)/$', ads_page, name='ads_page'),
    url(r'^new/$', add_new_ad, name='new_ad'),

]