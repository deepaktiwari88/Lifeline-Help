from django.db import models
from django.contrib.auth.models import User
import markdown

class Article(models.Model):

    title = models.CharField(max_length=255 , blank=False)
    created_by = models.CharField(max_length=255, default=None)
    date_created = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=2000 , blank=False)
    image = models.FileField(null=True , blank=True)

    def __str__(self):
        return self.title

    def get_summary(self):
        if len(self.description) > 2000:
            return '{0}...'.format(self.description[:2000])

        else:
            return self.description

    def get_summary_as_markdown(self):
        return markdown.markdown(self.get_summary(), safe_mode='escape')
