from django import forms
from .models import EducationBlogPost


class EducationBlogPostForm(forms.ModelForm):
    class Meta:
        model = EducationBlogPost
        fields = ('author_image', 'title', 'content', 'image', 'tag')
