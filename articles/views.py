from django.shortcuts import render, redirect
from . import models
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/register/login')
def index(request):
    articles = models.Article.objects.order_by('-date_created')
    context = {'articles': articles}
    return render(request, 'articles/articles.html', context)

@login_required(login_url='/register/login')
def write(request):

    if request.method == 'POST':

        form = ArticleForm(request.POST , request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user.get_username()

            form.save()
            return redirect('articles:art')


    else:
        form = ArticleForm()

    return render(request, 'articles/write.html', {'form':form})