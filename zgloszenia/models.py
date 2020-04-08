from django.db import models


# Create your models here.


class Zgloszenie(models.Model):
    opis = models.TextField(max_length=250)
    miejsce = models.CharField(max_length=50)
    imie = models.CharField(max_length=40)
    nazwisko = models.CharField(max_length=40)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.opis
