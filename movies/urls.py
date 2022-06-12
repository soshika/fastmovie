from django.urls import path
from movies import views
from signin import views as signin_views

urlpatterns = [
    path('', views.home_page_view, name='home'), # Notice the URL has been named
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('privacy/', views.PrivacyPageView.as_view(), name='privacy'),
    path('/contact', views.ContactPageView.as_view(), name='contact'),
    path('/explore', views.ExploreMoviesView.as_view(), name='explore-movies'),
    path('/detail', views.movie_detail, name='movie-detail')
]