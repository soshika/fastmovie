from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class SignupView(TemplateView):
    template_name = "signup.html"


class SignInView(TemplateView):
    template_name = 'signin.html'

class ForgetPasswordView(TemplateView):
    template_name = 'forget.html'

