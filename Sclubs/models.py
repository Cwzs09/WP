from __future__ import unicode_literals
from django.db import models

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