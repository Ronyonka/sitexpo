from django.test import TestCase
from .models import Profile,Project,Ratings
from django.contrib.auth.models import User

class ProfileTestCase(TestCase):
    def setUp(self):
        '''
        Profile set up method
        '''
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile(avatar='path/to/photo',user = self.user,bio='test bio')

    def test_instance(self):
        '''
        Tests for profile instance
        '''
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        '''
        Testing saving method
        '''
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

class ProjectTestCase(TestCase):
    def setUp(self):
        '''
        Project set up
        '''
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile(avatar='path/to/photo',user = self.user,bio='test bio')
        self.project = Project(title='test title',image='path/to/image',description='test description',owner=self.profile,url='https://something.com')

    def test_project_instance(self):
        '''
        Tests for project instance
        '''
        self.assertTrue(isinstance(self.project,Project))

class RatingsTestCase(TestCase):
    def setup(self):
        '''
        Ratings set up
        '''
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile(avatar='path/to/photo',user = self.user,bio='test bio')
        self.project = Project(title='test title',image='path/to/image',description='test description',owner=self.profile,url='https://something.com')
        self.rating= Ratings(project=self.project,user=self.user,review='test review',design=10,usability=10,content=10)

    def test_rating_instance(self):
        '''
        Tests for ratings instance
        '''
        self.assertTrue(isinstance(self.rating,Ratings))

