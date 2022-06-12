from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = "index.html"


class AboutPageView(TemplateView):
    template_name = "about.html"

class PrivacyPageView(TemplateView):
    template_name = 'privacy.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'

