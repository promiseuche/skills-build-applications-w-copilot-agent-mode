from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **options):
        # Drop all collections in the database using PyMongo
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
        db = client[settings.DATABASES['default']['NAME']]
        for collection_name in db.list_collection_names():
            db.drop_collection(collection_name)

        # Users
        users = [
            User.objects.create(email='alice@octofit.edu', name='Alice Johnson', password='password1'),
            User.objects.create(email='bob@octofit.edu', name='Bob Smith', password='password2'),
            User.objects.create(email='carol@octofit.edu', name='Carol Lee', password='password3'),
            User.objects.create(email='dan@octofit.edu', name='Dan Brown', password='password4'),
        ]

        # Teams
        team1 = Team.objects.create(name='Octofit Owls')
        team1.members.set([users[0], users[1]])
        team2 = Team.objects.create(name='Merington Mustangs')
        team2.members.set([users[2], users[3]])

        # Activities
        Activity.objects.create(user=users[0], activity_type='Running', duration=30)
        Activity.objects.create(user=users[1], activity_type='Cycling', duration=45)
        Activity.objects.create(user=users[2], activity_type='Swimming', duration=25)
        Activity.objects.create(user=users[3], activity_type='Walking', duration=60)

        # Workouts
        Workout.objects.create(name='Cardio Blast', description='High intensity cardio workout')
        Workout.objects.create(name='Strength Builder', description='Full body strength training')

        # Leaderboard
        Leaderboard.objects.create(team=team1, points=150)
        Leaderboard.objects.create(team=team2, points=120)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
