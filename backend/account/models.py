from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self, name, email, department, password , **other_fields):
        
        if not name:
            raise ValueError('Name can not be blank')
        if not email:
            raise ValueError("All users must have an email")
        if not department:
            raise ValueError('Department can not be blank, kindly fill in your department')

        email = self.normalize_email(email)
        user = self.model(name=name, email=email, department=department, password=password, **other_fields)
        user.set_password(password)
        user.save()
        
        return user

    def create_staffuser(self, name, email, department, password, **other_fields):
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_staff', True)

        if not other_fields.get('is_active'):
            raise ValueError('Staff users must have an active account')
        user = self.create_user(
            name=name,
            email=email,
            department=department,
            password=password,
            **other_fields
        )
        user.save()
        return user

    def create_superuser(self, name, email, department, password, **other_fields):
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if not other_fields.get('is_active'):
            raise ValueError('Staff users must have an active account')

        if not other_fields.get('is_staff'):
            raise ValueError('All Superusers must have a staff account')
        user = self.create_user(
            name=name,
            email=email,
            department=department,
            password = password,
            **other_fields
        )
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=250, unique=True)
    email = models.EmailField(verbose_name='Email', unique=True)
    department= models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email', 'department']
    USERNAME_FIELD = 'name'

    objects = UserManager()


    def __str__(self):
        return self.name
