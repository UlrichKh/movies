from django.urls import path
from movies.api.views import MovieCreateView, MovieListView

app_name = 'api_movies'

urlpatterns = [
    path('lst', MovieListView.as_view(), name='movies'),
    path('create', MovieCreateView.as_view(), name='create')
]
