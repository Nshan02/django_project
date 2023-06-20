from django.urls import reverse
from django.db import models
from accounts.models import Profile


class Post(models.Model):
    
    title = models.CharField(max_length=150)
    body = models.TextField()
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})
    
    def get_comments(self):
        comments = Comment.objects.filter(post = self)
        return comments
    
class Comment(models.Model):

    author = models.ForeignKey(Profile,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,related_name='post_comment',on_delete=models.CASCADE)
    text = models.CharField(max_length=500)

    def get_absolute_url(self):
        return reverse('home')
    
    def __str__(self):
        return self.text