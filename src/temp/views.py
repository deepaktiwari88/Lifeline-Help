from django.shortcuts import render,redirect
from .forms import LoginForm,SignUpForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required


def formhandleview(request):

    if request.method == "POST":

        if request.POST['check'] == "login":

            LoginFormRender = LoginForm(data=request.POST)

            if LoginFormRender.is_valid():
                user = LoginFormRender.get_user()
                login(request, user)
                return redirect('articles:art')

            else:
                SignUpFormRender = SignUpForm()

                context = {
                    'LoginFormRender': LoginFormRender,
                    'SignUpFormRender': SignUpFormRender
                }

                print(LoginFormRender.non_field_errors())
                return render(request, 'temp/join.html', context)

        elif request.POST['check'] == "signup":

            SignUpFormRender = SignUpForm(request.POST)
            print(request.POST)

            if SignUpFormRender.is_valid():
                user = SignUpFormRender.save(commit=False)

                password = SignUpFormRender.cleaned_data['password1']

                user.set_password(password)
                user.save()
                # login the user

                login(request, user)
                return redirect('articles:art')

            else:
                print(SignUpFormRender.errors.as_data() , "a")
                LoginFormRender = LoginForm()

                context = {
                    'LoginFormRender': LoginFormRender,
                    'SignUpFormRender': SignUpFormRender
                }
                return render(request, 'temp/join.html', context)

    else:
        LoginFormRender = LoginForm()
        SignUpFormRender = SignUpForm()

        context = {
            'LoginFormRender': LoginFormRender,
            'SignUpFormRender': SignUpFormRender
        }
        return render(request, 'temp/join.html', context)


@login_required(login_url='/register/login/')
def home(request):

    return render(request , 'temp/home.html',{})

@login_required(login_url='/register/login/')
def logout_view(request):

    logout(request)
    return redirect('temp:login')
