from django.db import models
from django.contrib.auth.models import User
import markdown

class Question(models.Model):

    asked_by = models.CharField(max_length=200, default=None)
    description = models.TextField(max_length=500)
    title = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)

    def get_answers(self):
        return Answer.objects.filter(question=self)

    def get_answers_count(self):
        return Answer.objects.filter(question=self).count()

    def get_description_as_markdown(self):
        return markdown.markdown(self.description, safe_mode='escape')

class Answer(models.Model):

    answered_by = models.CharField(max_length=500 , default=None)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    description = models.TextField(max_length=2000)
    create_date = models.DateTimeField(auto_now_add=True)

    def get_description_as_markdown(self):
        return markdown.markdown(self.description, safe_mode='escape')
