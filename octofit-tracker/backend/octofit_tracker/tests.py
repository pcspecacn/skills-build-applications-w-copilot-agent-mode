from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email='test@example.com', username='testuser', first_name='Test', last_name='User')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Team A', members=['test@example.com'])
        self.assertEqual(team.name, 'Team A')
        self.assertIn('test@example.com', team.members)

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(name='Running', user_email='test@example.com', duration=30, calories_burned=200)
        self.assertEqual(activity.name, 'Running')
        self.assertEqual(activity.duration, 30)

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(team='Team A', points=100, rank=1)
        self.assertEqual(leaderboard.team, 'Team A')
        self.assertEqual(leaderboard.rank, 1)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Push Ups', difficulty='Easy', description='Do 20 push ups')
        self.assertEqual(workout.name, 'Push Ups')
        self.assertEqual(workout.difficulty, 'Easy')
