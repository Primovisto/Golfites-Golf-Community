from django import forms
from .models import GolferProfile


class NewGolferForm(forms.ModelForm):
    class Meta:
        model = GolferProfile
        fields = (
                  'your_name',
                  'your_image',
                  'your_golf_club',
                  'current_handicap',
                  'lowest_handicap',
                  'about_my_golf',
                  'biggest_golfing_achievement',
                  'whats_in_your_bag',
                  'swing_video',
                  )
