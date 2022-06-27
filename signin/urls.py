from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup_view, name='signup'),
    path('signin', views.signin_view, name='signin'),
    path('forget', views.forget_password_view, name='forget'),
    path('verify-email', views.verify_email_view, name='verify-email')
]