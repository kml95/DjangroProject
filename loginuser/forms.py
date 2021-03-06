from django import forms
import re

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'Username', 'class' : 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password', 'class' : 'form-control'}))

    patternUsername = re.compile("^[a-zA-Z0-9]+$")
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

class RegisterForm(forms.Form):
    firstname = forms.CharField(label='First name', max_length=100, widget=forms.TextInput(attrs={'placeholder':'First name', 'class' : 'form-control'}))
    lastname = forms.CharField(label="Last Name", max_length=100, widget=forms.TextInput(attrs={'placeholder':'Last name', 'class' : 'form-control'}))
    email = forms.CharField(label="Email", max_length=100, widget=forms.TextInput(attrs={'placeholder':'e-mail', 'class' : 'form-control'}))
    username = forms.CharField(label="Username", max_length=100, widget=forms.TextInput(attrs={'placeholder':'Username', 'class' : 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password', 'class' : 'form-control'}), label="Password", max_length=100)

    patternFirstName = re.compile("^[A-Z][a-zA-Z]+$")
    patternLastName = re.compile("^[A-Z][a-zA-Z]+$")
    patternEmail = re.compile("[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$")   
    patternUsername = re.compile("^[a-zA-Z0-9]+$")
    patternPassword = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$")
    
    def clean_firstname(self):
        data = self.cleaned_data['firstname']

        if not self.patternFirstName.match(data):
            raise forms.ValidationError("Wrong first name! First name must begin with uppercase letter.")
        
        if len(data) < 3:
            raise forms.ValidationError("Too short username! Miniumum 3 signs.")

        return data

    def clean_lastname(self):
        data = self.cleaned_data['lastname']

        if not self.patternLastName.match(data):
            raise forms.ValidationError("Wrong last name! Last name must begin with uppercase letter.")
        
        if len(data) < 3:
            raise forms.ValidationError("Too short username! Miniumum 3 signs.")

        return data

    # def clean_email(self):
    #     data = self.cleaned_data['email']

    #     if not self.patternEmail.match(data):
    #         raise forms.ValidationError("Wrong email! Insert correct email, for example('jankowalski@wp.pl')")
        
    #     if len(data) < 3:
    #         raise forms.ValidationError("Too short username! Miniumum 3 signs.")

    #     return data    

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