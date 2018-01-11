from django import forms
from .models import GolferProfile


class NewGolferForm(forms.ModelForm):
    class Meta:
        model = GolferProfile
        fields = (
                  'name',
                  'image',
                  'golf_club',
                  'current_handicap',
                  'lowest_handicap',
                  'about_my_golf',
                  'biggest_golfing_achievement',
                  'whats_in_your_bag',
                  'swing',
                  )
