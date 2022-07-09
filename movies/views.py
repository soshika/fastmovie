import json
import urllib.request as ur

import requests
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

    trending_response = requests.get('http://45.148.120.241:9092/movies/trending')
    trending_dict = trending_response.json()
    trending = trending_dict['body']

    for t in trending:
        if t['imdbRating'] == 'N/A':
            t['imdbRating'] = 0.0
        t['imdbRating'] = float(t['imdbRating'])

    return render(request, 'index.html', {'generes': generes,
                                          'countries': countries,
                                          'movie': movie,
                                          'trending': trending})


def movie_detail(request, movie_name, movie_year):

    print(movie_name, movie_year)
    data = {'title': movie_name, 'year': int(movie_year)}
    response = requests.post('http://45.148.120.241:9092/movies/data', json=data)
    movie_response = response.json()
    print(movie_response)
    movie = movie_response['body']

    links = []
    links_section = []

    link_id = 1
    try:
        jdata = json.loads(movie['links'])

        for link in jdata:
            fix_link = str(link['url'])
            fix_link = fix_link.replace('sia://', 'https://siasky.net/')
            links.append(fix_link)
            # info = ur.urlopen(fix_link)
            # size = int(info.headers['Content-Length']) / 1000000000
            size = 1.7
            if link_id == 1:
                links_section.append({'quality': '1080P', 'size': round(size, 2), 'link': fix_link})
            else:
                links_section.append({'quality': '720P', 'size': round(size, 2), 'link': fix_link})

            link_id += 1
    except Exception as err:
        print(err)

    # print(links_section)
    #
    data = {'cnt': 10}
    response = requests.post('http://45.148.120.241:9092/movies/suggestion', json=data)
    suggestion_response = response.json()
    suggestions = suggestion_response['body']

    data = {'id': movie['id']}
    response = requests.post('http://45.148.120.241:9092/movies/review/list', json=data)
    reviews_response = response.json()
    reviews = reviews_response['body']

    if request.method == 'POST':
        title = request.POST['title'] or None
        message = request.POST['message'] or None
        rate = 9.4
        user_id = int(1)  # TODO: should dynamically fill it
        movie_id = movie['id']

        data = {'title': title, 'message': message, 'movie_id': movie_id, 'user_id': user_id, 'rate': rate}
        print(data)
        response = requests.post('http://45.148.120.241:9092/movies/review/save', json=data)
        response = response.json()
        print(response)
        return render(request, 'movie-detail.html', {'movie': movie, 'links': links, 'suggestions': suggestions, 'reviews': reviews, 'links_info': links_section})

    return render(request, 'movie-detail.html', {'movie': movie, 'links': links, 'suggestions': suggestions, 'reviews': reviews, 'links_info': links_section})


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


def explore_movies_view(request):
    top_response = requests.get('http://45.148.120.241:9092/movies/top')
    top_dict = top_response.json()
    top_movies = top_dict['body']

    final_top_movies = []
    for movie in top_movies:

        if movie['response'] == 'False' or movie['poster'] == 'N/A':
            continue
        final_top_movies.append(movie)

    for t in final_top_movies:
        if t['imdbRating'] == 'N/A':
            t['imdbRating'] = 0.0
        t['imdbRating'] = float(t['imdbRating'])

    return render(request, 'movie-list.html', {'movies': final_top_movies})


def search_view(request):
    if request.method == 'POST':
        data = {'query': request.POST['query']}
        response = requests.post('http://45.148.120.241:9092/movies/search', json=data)
        search_response = response.json()
        movies = search_response['body']
        return render(request, 'search.html', {'movies': movies})
    return render(request, "search.html")
