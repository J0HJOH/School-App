from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

User = get_user_model()

class TestUserAPI(TestCase):
    def setUp(self):
        User.objects.create(name ='kingsley', email='king@gmail.com', department='med')
        return super().setUp()

    def test_list(self):
        users = User.objects.all()
        self.assertTrue(users.exists())
        
