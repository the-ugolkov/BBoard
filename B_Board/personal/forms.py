from django import forms
from ads.models import Response


class ResponseForm(forms.ModelForm):
    accept = forms.BooleanField(widget=forms.CheckboxInput())

    class Meta:
        model = Response
        fields = ['accept']