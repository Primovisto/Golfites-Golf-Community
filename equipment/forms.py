from django import forms
from .models import Equipment


class NewEquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = (
                  'item',
                  'category',
                  'product_short_description',
                  'product_long_description',
                  'price',
                  'brand',
                  'brand_description',
                  'image')
