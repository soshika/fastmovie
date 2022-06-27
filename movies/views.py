from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView
from django.db import models

from . import  models

# Create your views here.


def home_page_view(request):

    gs = models.Genres.objects.all()
    generes = ['']
    for g in gs:
        generes.append(g.name)

    countries = models.Countries.objects.all()

    movie = models.Movie.objects.first()

    return render(request, 'index.html', {'generes': generes,
                                          'countries': countries,
                                          'movie': movie,
                                          'range': range(8)})


def movie_detail(request):
    # movie = models.Movie.objects.create(name='Downton Abbey: A New Era 2022',
    #                                     director='Simon Curtis',
    #                                     cast='Hugh Bonneville,Jim Carter,michelle dockery',
    #                                     generes='Drama, Romance',
    #                                     release_year='2022',
    #                                     country='USA, UK',
    #                                     description='The Crawley family goes on a grand journey to the South of France to uncover the mystery of the dowager countess\'s newly inherited villa.',
    #                                     url='https://siasky.net/GADorlimTyasUvr1yjPim_MrsjGNmXxNnPDxeI6hHbrrDQ',
    #                                     thumbnail='https://cdn-cloudflare.top/wp-content/uploads/2022/06/MV5BZDdjZjM1YWItNWRmOS00OTEzLWJmYjAtOGQzNTAyNmEwNDhjXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_SX500.jpg')
    # movie.save()

    movie = models.Movie.objects.first()
    print(movie.thumbnail)

    return render(request, 'movie-detail.html', {'movie': movie})

class AboutPageView(TemplateView):
    template_name = "about.html"


class PrivacyPageView(TemplateView):
    template_name = 'privacy.html'


def contact_view(request):
    if request.method == 'POST':
        name = request.POST['name'] or None
        email = request.POST['email'] or None
        subject = request.POST['subject'] or None
        message = request.POST['message']

        contact = models.Contact()
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()

    return render(request, 'contact.html')


class ContactPageView(TemplateView):
    template_name = 'contact.html'


class ExploreMoviesView(TemplateView):
    template_name = 'movie-list.html'

