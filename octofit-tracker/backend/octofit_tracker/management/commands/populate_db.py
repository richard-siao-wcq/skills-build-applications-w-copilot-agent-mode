from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', members=['Iron Man', 'Captain America', 'Thor'])
        dc = Team.objects.create(name='dc', members=['Superman', 'Batman', 'Wonder Woman'])

        # Create users
        User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel')
        User.objects.create(email='cap@marvel.com', name='Captain America', team='marvel')
        User.objects.create(email='thor@marvel.com', name='Thor', team='marvel')
        User.objects.create(email='superman@dc.com', name='Superman', team='dc')
        User.objects.create(email='batman@dc.com', name='Batman', team='dc')
        User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team='dc')

        # Create activities
        Activity.objects.create(user='Iron Man', type='run', duration=30, date='2026-03-12')
        Activity.objects.create(user='Captain America', type='cycle', duration=45, date='2026-03-12')
        Activity.objects.create(user='Thor', type='swim', duration=25, date='2026-03-12')
        Activity.objects.create(user='Superman', type='fly', duration=60, date='2026-03-12')
        Activity.objects.create(user='Batman', type='train', duration=40, date='2026-03-12')
        Activity.objects.create(user='Wonder Woman', type='fight', duration=35, date='2026-03-12')

        # Create leaderboard
        Leaderboard.objects.create(team='marvel', points=100)
        Leaderboard.objects.create(team='dc', points=90)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do pushups', suggested_for='marvel')
        Workout.objects.create(name='Flight', description='Fly around the city', suggested_for='dc')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
