import os
import sys
import django

if __name__ == "__main__":
    # Ensure the backend directory is in the Python path
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "octofit_tracker.settings")
    django.setup()
    from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

    def print_collection(name, queryset):
        print(f"\n{name}:")
        for obj in queryset:
            print(obj)

    print_collection("Users", User.objects.all())
    print_collection("Teams", Team.objects.all())
    print_collection("Activities", Activity.objects.all())
    print_collection("Leaderboards", Leaderboard.objects.all())
    print_collection("Workouts", Workout.objects.all())
