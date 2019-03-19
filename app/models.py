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

    @classmethod
    def get_profiles(cls):
        return cls.objects.all()


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
    def get_project_id(cls, id):
        project = Project.objects.get(pk=id)
        return project

    @classmethod
    def get_projects(cls):
        return cls.objects.all()

    @classmethod
    def filter_by_user(cls,owner):
        the_user = User.objects(username=owner)
        return cls.objects.filter(owner__id = the_user.id)

class Reviews(models.Model):
    text = models.TextField(max_length = 300, blank = True)
    project = models.ForeignKey(Project, related_name = "comments")
    author = models.ForeignKey(User, related_name = "author")
    created_date = models.DateTimeField(auto_now_add = True,null = True)


    def __str__(self):
        return self.text
 
    def save_review(self):
       self.save()  

    def delete_review(self):
        Review.objects.get(id = self.id).delete()
    
    @classmethod
    def get_reviews_by_projects(cls, id):
        reviews = Reviews.objects.filter(project__pk = id)
        return reviews
        
    @classmethod
    def get_reviews_by_projects(cls, id):
        reviews = Reviews.objects.filter(project__pk = id)
        return reviews
    
    # def get_comment(self, id):
    #     comments = Review.objects.filter(project_id =id)
    #     return comments

class Rating(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),

    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    design_rating = models.IntegerField(choices=RATING_CHOICES, default=0)
    usability_rating = models.IntegerField(choices=RATING_CHOICES, default=0)
    content_rating = models.IntegerField(choices=RATING_CHOICES, default=0)