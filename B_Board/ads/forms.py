from django import forms

from ads.models import Ad, Response


class AdsForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['category', 'author', 'title', 'text', 'content']


class ResForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['text']
