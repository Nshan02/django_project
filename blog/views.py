
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import DetailView,ListView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy,reverse
from .models import Post,Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required


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

# class PostCommentView(DetailView):
#     model = Post
#     template_name = 'post_comment.html'


class CommentCreateView(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    fields = ['text','post']


    def form_valid(self, form):

        form.instance.author = self.request.user.profile_user
        return super().form_valid(form)


# def comments(request,post_pk):


#     return reverse("profile_detail",pk= post_pk)


@login_required
def create_comments(request,pk):

    if request.method == 'POST':
    
        post = Post.objects.get(id = pk)
        if request.POST['text']:
            Comment.objects.create(
                                    author = request.user.profile_user,
                                    post = post,
                                    text = request.POST['text']
                                    )
    
        return redirect('post_detail',pk = pk)
