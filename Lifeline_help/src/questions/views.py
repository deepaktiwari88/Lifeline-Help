from django.shortcuts import get_object_or_404, redirect, render
from . import models
from django.contrib.auth.decorators import login_required
from .forms import QuestionForm , AnswerForm


@login_required(login_url='/register/login/')
def questions(request):

    que = models.Question.objects.order_by('-create_date')
    return render(request, 'questions/questions.html', {
        'questions': que,
    })


@login_required(login_url='/register/login/')
def AskQuestion(request ):

    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.asked_by = request.user.get_username()

            form.save()
            return redirect('questions:question')

    else:
        form = QuestionForm()

    return render(request , 'questions/ask.html' , {'form': form})


@login_required(login_url='/register/login/')
def question_spec(request, pk):
    question = get_object_or_404(models.Question, pk=pk)
    form = AnswerForm(initial={'question': question})

    return render(request, 'questions/question.html', {
        'question': question,
        'form': form
    })

@login_required(login_url='/register/login/')
def answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.question = models.Question.objects.get(pk= request.POST['question'])

            instance.answered_by = request.user.get_username()
            instance.save()
            return redirect('/question/{0}/'.format(instance.question.pk))

        else:
            question = form.cleaned_data.get('question')
            return render(request, 'questions/question.html', {
                'question': question,
                'form': form
            })

    else:
        return redirect('questions:question')