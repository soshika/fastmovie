import json
from tkinter.messagebox import NO
import urllib.request as ur

import requests
from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView
from django.db import models

from . import models

# Create your views here.

dev_endpoint = 'http://localhost:9092/'
rel_endpoint = 'http://45.148.120.241:9092/'


def home_page_view(request):

    genres_response = requests.get(rel_endpoint + 'movies/genres-list')
    genres_dict = genres_response.json()
    genres = genres_dict['body']

    countries_response = requests.get(rel_endpoint + 'movies/country-list')
    countries_dict = countries_response.json()
    countries = countries_dict['body']

    trending_response = requests.get(rel_endpoint +'movies/trending')
    trending_dict = trending_response.json()
    trending = trending_dict['body']

    for t in trending:
        if t['imdbRating'] == 'N/A':
            t['imdbRating'] = 0.0
        t['imdbRating'] = float(t['imdbRating'])

    return render(request, 'index.html', {'trending': trending, 'countries': countries, 'genres': genres})


def movie_detail(request, movie_name, movie_year):
    data = {'title': movie_name, 'year': int(movie_year)}
    response = requests.post(rel_endpoint + 'movies/data', json=data)
    movie_response = response.json()
    movie = movie_response['body']

    links = []
    links_section = []

    try:
        jdata = json.loads(movie['links'])

        for link in jdata:
            fix_link = str(link['url'])
            fix_link = fix_link.replace('sia://', 'https://siasky.net/')
            links.append(fix_link)
            size = ''
            quality = ''
            if 'fileSize' not in link:
                size = 'N/A'
            else :
                size = link['fileSize']
                size = str(round(size, 2))

            if 'quality' not in link:
                quality = 'N/A'
            else:
                quality = link['quality']
            
            links_section.append({'quality': quality, 'size': size, 'link': fix_link})

    except Exception as err:
        print(err)

    # print(links_section)
    #
    data = {'cnt': 10}
    response = requests.post(rel_endpoint + 'movies/suggestion', json=data)
    suggestion_response = response.json()
    suggestions = suggestion_response['body']

    data = {'id': movie['id']}
    response = requests.post(rel_endpoint + 'movies/review/list', json=data)
    reviews_response = response.json()
    reviews = reviews_response['body']

    if request.method == 'POST':
        title = request.POST['title'] or None
        message = request.POST['message'] or None
        rate = 9.4
        user_id = int(1)  # TODO: should dynamically fill it
        movie_id = movie['id']

        data = {'title': title, 'message': message, 'movie_id': movie_id, 'user_id': user_id, 'rate': rate}
        response = requests.post(rel_endpoint + 'movies/review/save', json=data)
        response = response.json()
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
    top_response = requests.get(rel_endpoint + 'movies/top')
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
    genres_response = requests.get(rel_endpoint + 'movies/genres-list')
    genres_dict = genres_response.json()
    genres = genres_dict['body']

    countries_response = requests.get(rel_endpoint + 'movies/country-list')
    countries_dict = countries_response.json()
    countries = countries_dict['body']

    if request.method == 'POST':
        if request.POST.get('query'):
            data = {'query': request.POST['query']}
            response = requests.post(rel_endpoint + 'movies/search', json=data)
            search_response = response.json()
            movies = search_response['body']
            return render(request, 'search.html', {'movies': movies, 'countries': countries, 'genres': genres})
        
    if request.method == 'GET':
        min_year = None
        max_year = None
        min_rate = None
        max_rate = None
        data = dict()
        if request.GET.get('min_year'):
            min_year = request.GET['min_year']

        if request.GET.get('max_year'):
            min_year = request.GET['max_year']

        if request.GET.get('min_rate'):
            min_year = request.GET['min_rate']
        
        if request.GET.get('max_rate'):
            min_year = request.GET['max_rate']

        if min_year != None:
            data['min_year'] = min_year

        if min_rate != None:
            data['min_rate'] = min_rate
        
        if max_year != None:
            data['max_year'] = max_year
        
        if max_rate != None:
            data['max_rate'] = max_rate

        response = requests.post(dev_endpoint + 'movies/search', json=data)
        search_response = response.json()
        movies = search_response['body']
        return render(request, 'search.html', {'movies': movies, 'countries': countries, 'genres': genres})
        
    return render(request, "search.html", {'countries': countries, 'genres': genres})
