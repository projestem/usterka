from django.urls import path

from zgloszenia import views

app_name = 'zgloszenia'
urlpatterns = [
    path('', views.index, name='index'),
    path('dodaj', views.UtworzZgloszenie.as_view(), name='dodaj'),
    path('lista', views.ListaZgloszen.as_view(), name='lista'),
    path('lista/<int:pk>', views.UsunZgloszenie.as_view(), name='usun')
]
