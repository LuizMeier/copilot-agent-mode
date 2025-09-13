from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Team, Activity, Leaderboard, Workout
from django.contrib.auth import get_user_model

User = get_user_model()

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Team.objects.create(name='Marvel')
        Team.objects.create(name='DC')
        User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass')
        Activity.objects.create(user='ironman', type='run', duration=30, team='Marvel')
        Leaderboard.objects.create(team='Marvel', points=55)
        Workout.objects.create(name='Hero HIIT', description='High intensity workout for heroes')

    def test_api_root(self):
        response = self.client.get(reverse('api_root'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_teams_list(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_users_list(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_activities_list(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_leaderboard_list(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_workouts_list(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
