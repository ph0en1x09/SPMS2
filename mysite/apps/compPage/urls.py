from django.urls import path

from . import views

app_name = 'compPage'
urlpatterns = [
    path('', views.index, name='index'),
]
