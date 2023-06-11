from django.contrib import admin
from django.urls import path
from .views import PostCreateView,PostDetailView,HomePageView,PostDeleteview,PostUpdateView,CssPageView

urlpatterns = [
    path('',HomePageView.as_view(),name= 'home'),
    path('create/',PostCreateView.as_view(),name= "post_create"),
    path('detail/<int:pk>/',PostDetailView.as_view(),name= 'post_detail'),
    path('delete/<int:pk>/',PostDeleteview.as_view(),name= 'post_delete'),
    path('update/<int:pk>/',PostUpdateView.as_view(),name= 'post_update'),
    path('css/',CssPageView.as_view(),name='css')
]


