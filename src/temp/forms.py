from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class LoginForm(AuthenticationForm, forms.Form):
    check = forms.CharField(widget=forms.HiddenInput)


class SignUpForm(UserCreationForm, forms.Form):
    check = forms.CharField(widget=forms.HiddenInput)
