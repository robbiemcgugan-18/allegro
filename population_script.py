import os
import datetime
import django
from eventastic.models import User, UserProfile, Level

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eventastic_project.settings')
django.setup()

# Clear the existing database
def clear_db():
    UserProfile.objects.filter().delete()
    User.objects.filter().delete()
    Level.objects.filter().delete()


def generate_data():
    # generate a user
    user1 = User(username="robbiemcgugan", first_name="Robbie", last_name="McGugan", email="robbiemcgugan@gmail.com")
    user1.set_password("default123")

    user1.save()

    # generate a user profile
    profile1 = UserProfile(user=user1, DOB=datetime.datetime(1990, 5, 18))
