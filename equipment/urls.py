from django.conf.urls import url
from .views import all_equipment, equipment_page, search_names

urlpatterns = [

    url(r'^$', all_equipment, name='equipment'),
    url(r'^(?P<id>\d+)/$', equipment_page, name='equipmentpage'),
    url(r'^equipment/search/$', search_names, name='search'),

]
