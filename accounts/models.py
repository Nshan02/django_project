from django.urls import reverse
from django.db import models
from datetime import date


class Profile(models.Model):

    user = models.OneToOneField('auth.user',related_name="profile_user",on_delete=models.CASCADE)
    category = models.CharField(max_length=150)
    user_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    birth_date = models.DateField()
    

    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        
        if today.month < self.birth_date.month or today.month == self.birth_date.month and today.day < self.birth_date.day:
            age -= 1

        return age
    
    def __str__(self):
        return f"{self.user_name} {self.last_name}" 
    
    def get_absolute_url(self):
        return reverse('profile_detail',kwargs={'pk':self.pk})
    
    def get_friends(self):
        friendship1 = Friendship.objects.filter(user1 = self)
        friendship2 = Friendship.objects.filter(user2 = self)
        friends_list = []

        for friend in friendship1:
            friends_list.append(friend.user2)

        for friend in friendship2:
            friends_list.append(friend.user1)

        return friends_list
    

class Friendship(models.Model):
    user1 = models.ForeignKey(Profile, related_name='friendships', on_delete=models.CASCADE)
    user2 = models.ForeignKey(Profile, related_name='friends', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user1', 'user2')

    def __str__(self):
        return f'{self.user1} is friend to {self.user2}' 
    
    def get_absolute_url(self):
        return reverse('profile_detail',kwargs={'pk':self.pk})
        
    
        
 