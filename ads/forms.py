from django import forms
from .models import Ad


class NewAdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = (
                  'name',
                  'product_short_description',
                  'location',
                  'price',
                  'views',
                  'image')