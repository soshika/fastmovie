from django.urls import path
from . import views

urlpatterns = [
    path('', views.SignupView.as_view(), name='signup'),
    path('/signin', views.SignInView.as_view(), name='signin'),
    path('/forget', views.ForgetPasswordView.as_view(), name='forget'),
]