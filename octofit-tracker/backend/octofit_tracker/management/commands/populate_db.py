from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Borrar datos existentes
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Equipos
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Usuarios
        ironman = User.objects.create(name='Tony Stark', email='tony@marvel.com', team='Marvel')
        spiderman = User.objects.create(name='Peter Parker', email='peter@marvel.com', team='Marvel')
        superman = User.objects.create(name='Clark Kent', email='clark@dc.com', team='DC')
        batman = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team='DC')

        # Actividades
        Activity.objects.create(user='Tony Stark', type='Running', duration=30)
        Activity.objects.create(user='Peter Parker', type='Cycling', duration=45)
        Activity.objects.create(user='Clark Kent', type='Swimming', duration=60)
        Activity.objects.create(user='Bruce Wayne', type='Boxing', duration=40)

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=75)
        Leaderboard.objects.create(team='DC', points=100)

        # Workouts
        Workout.objects.create(name='Push Ups', description='Upper body exercise')
        Workout.objects.create(name='Squats', description='Lower body exercise')
        Workout.objects.create(name='Plank', description='Core strength exercise')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully'))
