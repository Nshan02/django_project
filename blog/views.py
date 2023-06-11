from django.shortcuts import render
from django.views.generic import DetailView,ListView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts_list'

class PostCreateView(CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = ['title','body']

    def form_valid(self, form): 
        form.instance.profile = self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostDeleteview(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title','body']


class CssPageView(ListView):
    model = Post
    template_name = 'base1.html'
