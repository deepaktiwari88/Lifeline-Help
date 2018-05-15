from django import forms

from .models import Article
from django.contrib.auth.forms import AuthenticationForm

class ArticleForm(forms.ModelForm):

    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Title'}),
        max_length=255)

    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Description'}),
        max_length=4000)


    class Meta:
        model = Article
        fields = ['title' , 'description' , 'image']