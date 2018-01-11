from django import forms
from .models import GolferProfile


class NewGolferForm(forms.ModelForm):
    class Meta:
        model = GolferProfile
        fields = (
                  'name',
                  'handicap',
                  'golf_club',
                  'whats_in_your_bag',
                  )
