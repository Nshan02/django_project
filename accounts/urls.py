from django.contrib import admin
from django.urls import path
from .views import (ProfileCreateView,
                    ProfileDetailView,
                    SignUpView,
                    ProfileUpdateView,
                    AddFriend,
                    deletefriend,
                    search_users,
                    )

urlpatterns = [
    path('signup/',SignUpView.as_view(),name='signup'),
    path('create/',ProfileCreateView.as_view(),name='create_profile'),
    path('detail/<int:pk>/',ProfileDetailView.as_view(),name='profile_detail'),
    path('update/<int:pk>/',ProfileUpdateView.as_view(),name='profile_update'),
    path('add-friend/<int:user_id>/', AddFriend, name='add_friend'),
    path('delete-friend/<int:user_id>/',deletefriend,name= 'delete_friend'),
    path('users/',search_users,name='users')

]


