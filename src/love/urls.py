from django.urls import path

from . import views
app_name = "love"
urlpatterns = [
    path('', views.ind, name="ind"),
    path('val', views.valnt, name='val'),
]