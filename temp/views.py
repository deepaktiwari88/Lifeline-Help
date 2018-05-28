from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

def signup_view(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user.set_password(password)
            user.save()
            #login the user


            login(request , user)
            return redirect('articles:art')

    else:
        form = UserCreationForm()
    return render(request , 'temp/join.html', {'form':form})

def login_view(request):
    if request.method == "POST":

        form = AuthenticationForm(data=request.POST)
        if form.is_valid():

            user = form.get_user()
            login(request, user)
            return redirect('articles:art')
    else:
        form = AuthenticationForm()

    return render(request , 'temp/login.html' , {'form':form})


@login_required(login_url='/register/login/')
def home(request):

    return render(request , 'temp/home.html',{})

@login_required(login_url='/register/login/')
def logout_view(request):

    logout(request)
    return redirect('temp:login')
