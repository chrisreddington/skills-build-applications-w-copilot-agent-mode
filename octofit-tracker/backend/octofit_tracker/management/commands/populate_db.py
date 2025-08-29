from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            {'email': 'ironman@marvel.com', 'username': 'IronMan', 'team': 'Marvel'},
            {'email': 'captain@marvel.com', 'username': 'CaptainAmerica', 'team': 'Marvel'},
            {'email': 'batman@dc.com', 'username': 'Batman', 'team': 'DC'},
            {'email': 'superman@dc.com', 'username': 'Superman', 'team': 'DC'},
        ]
        for u in users:
            User.objects.create_user(email=u['email'], username=u['username'], password='test1234')

        # Create activities
        activities = [
            {'name': 'Run', 'user_email': 'ironman@marvel.com', 'team': 'Marvel'},
            {'name': 'Swim', 'user_email': 'captain@marvel.com', 'team': 'Marvel'},
            {'name': 'Fly', 'user_email': 'superman@dc.com', 'team': 'DC'},
            {'name': 'Detective Work', 'user_email': 'batman@dc.com', 'team': 'DC'},
        ]
        for a in activities:
            Activity.objects.create(**a)

        # Create workouts
        workouts = [
            {'name': 'Pushups', 'description': 'Do 50 pushups'},
            {'name': 'Sprints', 'description': 'Run 5 sprints'},
        ]
        for w in workouts:
            Workout.objects.create(**w)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
