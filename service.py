# services.py
from django.db import IntegrityError
from django.contrib.auth.models import User
from .models import UserProfile


def register_user(username, lastname, email, password):
    try:
        new_user = User.objects.create_user(
            username=username, email=email, password=password)

        user_profile = UserProfile.objects.create(
            user=new_user, lastname=lastname)

        print("User and UserProfile saved successfully")
        print(f"User ID: {new_user.id}, UserProfile ID: {user_profile.id}")

        return user_profile
    except IntegrityError as e:
        print(f"IntegrityError: {e}")
        raise
