from django import forms
from .models import Ad


class NewAdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = (
                  'your_name',
                  'item_name',
                  'item_price',
                  'item_image',
                  'published_date',
                  'contact_email',
                  'product_short_description',
                  'your_location',
                  )
