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
    # print(request.META['HTTP_HOST'])
    if form.is_valid():
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        department = form.cleaned_data.get("department")
        password1 = form.cleaned_data.get("password1")

        user = User.objects.create(name = name, email = email, department = department, password = password1)
        user.set_password(password1)
        user.save()
        return redirect('account:signin')
        
        

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
        return redirect('account:dashboard')
    else:
        form = UserLoginForm(request)
    context = {
        'form': form
    }
    
    return render(request, 'login.html', context)



def apiDocs(request, *args, **kwargs):
    context = {
        'message': "name: name: users name <br> request_message: request.META.HTTP_HOST"
        #     'name: name: user's name
        # 'request_message': request.META.HTTP_HOST
        # 'email': "email: user's email",
        # 'department': "department: user's department",
        # 'password': "password: user's password
        # "
    }
    return render(request, 'api_docs.html', context)