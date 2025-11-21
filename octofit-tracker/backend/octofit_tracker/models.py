
from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    class Meta:
        app_label = 'octofit_tracker'

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.JSONField(default=list)  # List of user emails
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    name = models.CharField(max_length=100)
    user_email = models.EmailField()
    team_name = models.CharField(max_length=100, blank=True, null=True)
    duration = models.IntegerField()  # in minutes
    calories_burned = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    rank = models.IntegerField(default=0)
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    suggested_for = models.JSONField(default=list)  # List of user emails
    class Meta:
        app_label = 'octofit_tracker'
