from django import forms
from .models import Ad


class NewAdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = (
                  'advertiser',
                  'item',
                  'contact_email',
                  'published_date',
                  'product_short_description',
                  'your_location',
                  'item_price',
                  'views',
                  'item_image')
