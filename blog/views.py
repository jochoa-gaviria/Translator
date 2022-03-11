from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

class blogView(generic.DetailView):
    model = Post
    template_name = 'blog.html'

class aboutView(generic.TemplateView):
    template_name = 'about.html'

class postList(generic.ListView):
    # queryset = Post.objects.all()
    queryset = Post.objects.filter(status=1).order_by('-dateCreate')
    # queryset = Post.objects.order_by('dateCreate')
    template_name = 'index.html'