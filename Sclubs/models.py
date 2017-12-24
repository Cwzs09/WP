from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User



class University(models.Model):
    University_Name = models.CharField(max_length=150)

    def __str__(self):
        return self.University_Name

class Club(models.Model):
    University = models.ForeignKey(University , on_delete=models.CASCADE)
    Chairman = models.CharField(max_length=50)
    Vice_Chairman = models.CharField(max_length=50)
    Genre = models.CharField(max_length=50)
    Club_email = models.CharField(max_length=100)
    Club_Logo = models.CharField(max_length=1000)
    Club_Name = models.CharField(max_length=200)

    def __str__(self):
        return self.Club_Name

class Member(models.Model):
    Club = models.ForeignKey(Club, on_delete=models.CASCADE)
    Member_name = models.CharField(max_length=100)

    def __str__(self):
        return self.Member_name

    #additionals

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to="user_imgs", blank=True)

    def __str__(self):
        return "{} - {}".format(self.user.username, self.id)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Comment(models.Model):
    title = models.CharField(max_length=150, blank=True)
    body = models.TextField(blank=True)
    rating = models.IntegerField(blank=True)


