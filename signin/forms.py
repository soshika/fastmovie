from django import forms


class SignupForm(forms.Form):
    username = forms.CharField(max_length=128)
    email = forms.EmailField(max_length=128)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=128, widget=forms.PasswordInput())
