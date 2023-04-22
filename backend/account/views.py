from django.shortcuts import render, redirect
from .forms import UserRegister, UserLoginForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib import messages
from datetime import timedelta
User = get_user_model()

# Create your views here.
def home(request):
    pass


def Register(request, *args, **kwargs):
    form = UserRegister(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        department = form.cleaned_data.get("department")
        password1 = form.cleaned_data.get("password1")

        user = User.objects.create(name = name, email = email, department = department, password = password1)
        user.set_password(password1)
        user.save()
        messages.success(request, "You successfully created an account with us")
        form = UserRegister()

    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def loginView(request, *args, **kwargs):
    form = UserLoginForm(request, data = request.POST)
    
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        remeber_me = request.POST.get("checkbox")
        print(remeber_me)
        if remeber_me == "on":
            request.session.set_expiry(timedelta(days=90))

        # messages.success(request, f'You have successfully login as {request.user.username}')
        return redirect('account:home')
    else:
        form = UserLoginForm(request)
    context = {
        'form': form
    }
    
    return render(request, 'login.html', context)



