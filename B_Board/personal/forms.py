from allauth.account.forms import SignupForm
from django import forms
from ads.models import Response


class ResponseForm(forms.ModelForm):
    accept = forms.BooleanField(widget=forms.CheckboxInput())

    class Meta:
        model = Response
        fields = ['accept']


class MySignupForm(SignupForm):
    def save(self, request):
        user = super(MySignupForm, self).save(request)
        user.is_active = False
        user.save()
        return user