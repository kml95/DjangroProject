from django import forms
import re

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, label="Password", max_length=100)

    patternUsername = re.compile("^[a-z0-9]+$")
    patternPassword = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$")
    
    def clean_username(self):
        data = self.cleaned_data['username']

        if not self.patternUsername.match(data):
            raise forms.ValidationError("Wrong username! Username must contains at least l lowercase letter and number.")
        
        if len(data) < 6:
            raise forms.ValidationError("Too short username! Miniumum 6 signs.")

        return data

    def clean_password(self):
        data = self.cleaned_data['password']

        if len(data) < 8:
            raise forms.ValidationError("Too short password! Minimum 8 signs.")
            
        if not self.patternPassword.match(data):
            raise forms.ValidationError("Wrong password! Password must contains at least l lowercase letter, uppercase letter and number.")

        return data