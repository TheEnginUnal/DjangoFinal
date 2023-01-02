from django import forms 
from django.contrib.auth.forms import AuthenticationForm


class RegisterForm(forms.ModelForm):

    userName = forms.CharField(label="Enter Username", min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={
        'required' : 'Bir E-Mail adresi girmelisin'
    })
    firstName = forms.CharField(label="Enter your First Name", min_length=3, max_length=50)
    lastName = forms.CharField(label = "Enter your Last Name", min_length=3, max_length= 50 )
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    repassword = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)


