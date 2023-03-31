from django import forms

from ads.models import Ad


class AdsForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['category', 'author', 'title', 'text', 'content']
