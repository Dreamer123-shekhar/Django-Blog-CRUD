from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Post ( models.Model ) :
    title = models.CharField ( max_length=255 )
    author = models.ForeignKey ( User, on_delete=models.CASCADE )
    body = models.TextField ()

    def __str__(self) :
        return self.title + ' ' + str ( self.author )  # turning object into string

    def get_absolute_url(self):
        return reverse('article-detail',args=(str(self.id)) )
        #or can just do return reverse('home') if you want it to go thome page