from django.db import models
from django.utils import timezone

# Create your models here.
class Convcon(models.Model):
    author = models.ForeignKey('auth.User')
    connector = models.CharField(max_length=100)
    contransl = models.CharField(max_length=100)
    examplesent = models.CharField(max_length=200)
    exampletransl = models.CharField(max_length=200)
    usagenotes = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    audiofilulinkki = models.CharField(max_length=200)




    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.connector


