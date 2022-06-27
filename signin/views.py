import requests
import json

from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import SignupForm

# Create your views here.


def users_verify_view(request, token):
    if request.method == "GET":
        print(token)


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username'] or None
        email = request.POST['email'] or None
        password = request.POST['password']
        confrim_password = request.POST['confrim_password']

        if password != confrim_password:
            print('password is mismatch')

        post_data = {'username': username,
                     'email': email,
                     'password': password}
        response = requests.post('http://localhost:9092/users', json=post_data)
        content_byte = response.content
        content = json.loads(content_byte.decode('utf-8'))
        if content['header']['status'] == 200:
            return render(request, 'verify-email.html')
    else:
        pass

    return render(request, 'signup.html')


def verify_email_view(request):
    return render(request, 'verify-email.html')


def signin_view(request):
    print('hello')
    if request.method == 'POST':
        print('post')
        email = request.POST['email'] or None
        password = request.POST['password']

        post_data = {'email': email,
                     'password': password}

        response = requests.post('http://localhost:9092/users/login', json=post_data)
        content_byte = response.content
        content = json.loads(content_byte.decode('utf-8'))

        if content['header']['status'] == 200:
            print('helloooooo')
            return render(request, 'index.html')

    return render(request, 'signin.html')


def forget_password_view(request):
    if request.method == 'POST':
        email = request.POST['email'] or None
        post_data = {'email': email}

        response = requests.post('http://localhost:9092/users/forget', json=post_data)
        content_byte = response.content
        content = json.loads(content_byte.decode('utf-8'))

        if content['header']['status'] == 200:
            return render(request, 'index.html')

    return render(request, 'forget.html')


class SignInView(TemplateView):
    template_name = 'signin.html'
