from rest_framework import serializers
from .models import Profile,Project
from django.contrib.auth.models import User

class ProjectSerializer(serializers.ModelSerializer):


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= Project
        fields = ['bio']
class UserSerializer(serializers.ModelSerializer):
     profile = ProfileSerializer('profile')
     class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'email', 'profile']

class PrflSerializer(serializers.ModelSerializer):
   user = UserSerializer('user')
   class Meta:
      model = Profile
      fields = ['bio','user']

class  ProjectSerializer(serializers.ModelSerializer):
   owner = PrflSerializer('profile')

   class Meta:
      model = Project
      fields = ['title','description','url','owner']


