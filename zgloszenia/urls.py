from django.urls import path

from zgloszenia import views

app_name = 'zgloszenia'
urlpatterns = [
    path('', views.index, name='index'),
    path('dodaj', views.UtworzZgloszenie.as_view(), name='dodaj')
]
