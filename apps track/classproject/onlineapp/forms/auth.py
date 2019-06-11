from django import forms
from django.forms import TextInput,DateInput,EmailInput,CheckboxInput,PasswordInput
from onlineapp.models import *
#from django.db import models
class loginform(forms.Form):

    username=forms.CharField(
        required=True,
        label="username",

        widget=TextInput(attrs={'class':'input is-primary','placeholder':"write username"}),
    )
    password=forms.CharField(
        required=True,
        label="password",
        widget=PasswordInput(attrs={'class':'input is-primary','placeholder':"enter password"}),
    )

class signupform(forms.Form):

    firstname = forms.CharField(
        required=True,

        label="firstname",
        widget=TextInput(attrs={'class':'input is-primary','placeholder':"enter firstname"}),
    )
    lastname = forms.CharField(
        required=True,
        label="lastname",
        widget=TextInput(attrs={'class':'input is-primary','placeholder':"enter lastname"}),
    )
    username = forms.CharField(
        required=True,
        label="username",
        widget=TextInput(attrs={'class':'input is-primary','placeholder':"enter username"}),
    )
    password = forms.CharField(
        required=True,
        label="password",
        widget=PasswordInput(attrs={'class':'input is-primary','placeholder':"enter password"}),
    )

