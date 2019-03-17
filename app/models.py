from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    avatar = models.ImageField(null=True, upload_to='avatar/')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f'{self.user.username}'


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Project(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='projects/')
    description = models.TextField(max_length=500)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    url = models.CharField(max_length=100)
     
    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    def update_description(self,desc):
        self.description = desc
        self.save()

    @classmethod
    def search_projects(cls, title):
        projects = Project.objects.filter(title__icontains = title)
        return projects

    @classmethod
    def get_projects(cls):
        return cls.objects.all()

    @classmethod
    def filter_by_user(cls,owner):
        the_user = User.objects(username=owner)
        return cls.objects.filter(owner__id = the_user.id)