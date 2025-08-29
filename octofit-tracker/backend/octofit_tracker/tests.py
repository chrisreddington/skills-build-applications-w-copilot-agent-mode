from django.test import TestCase
from .models import Team, Activity, Workout, Leaderboard
from django.contrib.auth import get_user_model

User = get_user_model()

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Test Team")
        self.assertEqual(team.name, "Test Team")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(name="Run", user_email="test@example.com", team="Test Team")
        self.assertEqual(activity.name, "Run")

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Pushups", description="Do 20 pushups")
        self.assertEqual(workout.name, "Pushups")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(team="Test Team", points=100)
        self.assertEqual(leaderboard.team, "Test Team")
