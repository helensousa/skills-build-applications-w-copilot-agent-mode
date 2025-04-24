from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User.objects.create(email="john.doe@example.com", name="John Doe", age=25)
        user2 = User.objects.create(email="jane.smith@example.com", name="Jane Smith", age=30)

        # Create test teams
        team1 = Team.objects.create(name="Team Alpha", members=["John Doe", "Jane Smith"])

        # Create test activities
        Activity.objects.create(user=user1, type="Running", duration=30)
        Activity.objects.create(user=user2, type="Cycling", duration=45)

        # Create test leaderboard entries
        Leaderboard.objects.create(user=user1, score=100)
        Leaderboard.objects.create(user=user2, score=150)

        # Create test workouts
        Workout.objects.create(name="Push-ups", description="Do 20 push-ups")
        Workout.objects.create(name="Squats", description="Do 30 squats")

        self.stdout.write(self.style.SUCCESS('Database populated with test data'))
