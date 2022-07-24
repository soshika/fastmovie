from django.urls import path
from movies import views
from signin import views as signin_views

urlpatterns = [
    path('', views.home_page_view, name='home'), # Notice the URL has been named
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('privacy/', views.PrivacyPageView.as_view(), name='privacy'),
    path('contact/', views.contact_view, name='contact'),
    path('explore/<int:page>/', views.explore_movies_view, name='explore'),
    path('explore/country/<str:country>/', views.explore_country_movies_view, name='explore-country'),
    path('explore/actor/<str:actor>/', views.explore_actor_movies_view, name='explore-actor'),
    path('explore/director/<str:director>/', views.explore_director_movies_view, name='explore-director'),
    path('explore/genre/<str:genre>/<int:page>/', views.explore_genre_movies_view, name='explore-genre'),
    path('explore/top', views.explore_top_movies_view, name='explore-movies'),
    path('detail/<str:movie_name>/<str:movie_year>/', views.movie_detail, name='movie-detail'),
    path('search/', views.search_view, name='search')
]