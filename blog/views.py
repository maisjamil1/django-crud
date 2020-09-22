from django.shortcuts import render
from .models import Post
from django.views.generic import TemplateView,ListView, DetailView

# Create your views here.
class BlogListView(ListView):
    template_name = 'home.html'
    model=Post

class BlogDetailView(DetailView):
    template_name = 'details.html'
    model=Post

