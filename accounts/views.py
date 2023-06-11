from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView,DetailView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Friendship
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest,HttpResponse



class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy('login')

class ProfileCreateView(CreateView):
    model = Profile
    template_name = "create_profile.html"
    fields = ["category", "user_name",'last_name','birth_date']

    def form_valid(self, form): 
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile_detail.html'
    

class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = 'profile_update.html'
    fields = ['category','user_name','last_name','birth_date']


@login_required
def AddFriend(request, user_id):
    friend_profile = get_object_or_404(Profile, id=user_id)
    if request.method == 'POST':
        Friendship.objects.create(
            user1=request.user.profile_user,
            user2=friend_profile,
        )
        return HttpResponse(f'{friend_profile.user_name} is added to your friends')
    else:
        return HttpResponseBadRequest('Invalid request method')


    