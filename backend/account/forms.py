from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

User = get_user_model()

class AdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = '__all__'

    def clean_data(self):
        return self.initial['password']


class UserRegister(UserCreationForm):
    # password = forms.CharField(widget=forms.PasswordInput())
    # confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['name', 'email', 'department', 'password1', 'password2']
        help_texts = {
            'password1': None,
            "password2": None,
        }
    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        try:
            validate_password(password)
            return password
        except Exception as e:
            raise forms.ValidationError(f'{e}')
        

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 != password2:
            raise forms.ValidationError('The both password must match')
        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email__iexact = email):
            raise forms.ValidationError('This email already exists. kindly choose another email ')
        return email

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if User.objects.filter(name__iexact = name):
            raise forms.ValidationError("An account has been created with this name")
        return name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'user-name', 'name': 'name', 'type':'text', "label": "name"})
        self.fields['email'].widget.attrs.update({'class': 'user-email', 'name': 'email', 'type': 'email', "label": "email"})
        self.fields['password1'].widget.attrs.update({'class': 'user-password', 'name': 'password', "type":"password", "label": "password"})
        self.fields['password2'].widget.attrs.update({'class': 'confirm-password', 'name': 'confirm-password', "type":"password", "label": "Confirm password"})
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['name'].errors = None


class UserLoginForm(AuthenticationForm):
    # remeber_me = forms.CharField(widget=forms.BooleanField())

    class Meta:
        fields = ['username', 'password']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({"class": "login-password"})
        self.fields['username'].widget.attrs.update({"class":"login-input"})


