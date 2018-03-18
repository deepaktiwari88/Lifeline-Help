from django.forms import ModelForm
from django import forms
from  .models import Question,Answer

class QuestionForm(ModelForm):

    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
        max_length=255)

    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        max_length=4000)

    class Meta:
        model = Question
        fields = ['title', 'description']

class AnswerForm(ModelForm):

    question = forms.ModelChoiceField(widget=forms.HiddenInput(),
                                      queryset=Question.objects.all())

    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        max_length=4000)

    class Meta:

        model = Answer
        fields = [ 'question', 'description']