from django.contrib.auth.models import User
# from django.db.models import *
from django.db import models


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='candidate_pics')


class VotingSession(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    year = models.IntegerField()
    country = models.CharField(max_length=100)
    image = models.ImageField(upload_to='voting_pics')
    candidates = models.ManyToManyField('Candidate', related_name='candidates')


class VoteUser(models.Model):
    candidate = models.ForeignKey('Candidate', on_delete=models.CASCADE)
    voting_session = models.ForeignKey('VotingSession', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
