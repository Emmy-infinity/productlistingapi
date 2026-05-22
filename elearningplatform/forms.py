from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class createuserform(UserCreationForm):
    class meta:
        model=User
        fields=['username','password','email']