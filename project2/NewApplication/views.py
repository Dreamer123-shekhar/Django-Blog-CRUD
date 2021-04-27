from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView, UpdateView,DeleteView, TemplateView
from .models import Post
from django.urls import reverse_lazy


class HomeView ( ListView ) :
    model = Post
    template_name = 'index.html'


class ArticleView ( DetailView ) :
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'

class EditView(UpdateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'

class Deletion(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    fields = '__all__'
    success_url = reverse_lazy('home')

class AboutPageView(TemplateView):
    template_name = 'about.html'
