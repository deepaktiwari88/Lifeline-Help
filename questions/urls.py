from django.conf.urls import url
from . import views

app_name = 'questions'

urlpatterns = [
    url(r'^$', views.questions, name='question'),
    url(r'^ask/$', views.AskQuestion, name='ask'),
    url(r'^(?P<pk>[0-9]+)/$', views.question_spec,name='question_spec'),
    url(r'^(?P<pk>[0-9]+)$', views.question_spec,name='question_spec'),
    url(r'^answer/$', views.answer, name='answer'),

]
