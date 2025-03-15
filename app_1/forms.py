from django import forms
from .models import User


class NewsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['author', 'short_info', 'description', 'image']
