from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass'),
            User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='pass'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='pass'),
            User.objects.create_user(username='superman', email='superman@dc.com', password='pass'),
        ]

        # Activities
        Activity.objects.create(name='Run', user_email='ironman@marvel.com')
        Activity.objects.create(name='Swim', user_email='cap@marvel.com')
        Activity.objects.create(name='Fly', user_email='superman@dc.com')
        Activity.objects.create(name='Fight', user_email='batman@dc.com')

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=200)
        Leaderboard.objects.create(team='DC', points=180)

        # Workouts
        Workout.objects.create(name='Pushups', difficulty='Medium')
        Workout.objects.create(name='Sprints', difficulty='Hard')
        Workout.objects.create(name='Yoga', difficulty='Easy')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
