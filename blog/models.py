from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

sections = (('Programming', 'Programming'), ('Anime','Anime'), ('Gaming','Gaming'))
programming_topics = (('Javascript','Javascript'), ('Python','Python'),('React', 'React'), ('Django','Django'),)

class Post(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """    
    
   
    title = models.CharField(max_length=300)
    content = models.TextField()
    section = models.CharField(max_length=12, choices=sections)
    # topic = models.CharField(max_length=11, choices=programming_topics, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    minutes_to_read = models.IntegerField(default=5)
    image = models.ImageField(
        upload_to = 'post_images',
        default='bloglist-1.jpg',
        max_length=100
        )
    
    def __str__(self):
        return self.title
    
    
# class AnimePost(models.Model):
#     """_summary_

#     Args:
#         models (_type_): _description_
#     """    
    
#     title = models.CharField(max_length=300)
#     content = models.TextField()
#     date_posted = models.DateTimeField(default=timezone.now)
#     minutes_to_read = models.IntegerField(default=5)
#     image = models.ImageField(
#         upload_to = 'anime/post_images',
#         default='bloglist-1.jpg',
#         max_length=100
#         )
    
#     def __str__(self):
#         return self.title
    
    
# class GamingPost(models.Model):
#     """_summary_

#     Args:
#         models (_type_): _description_
#     """    
    
#     title = models.CharField(max_length=300)
#     content = models.TextField()
#     date_posted = models.DateTimeField(default=timezone.now)
#     minutes_to_read = models.IntegerField(default=5)
#     image = models.ImageField(
#         upload_to = 'anime/post_images',
#         default='bloglist-1.jpg',
#         max_length=100
#         )
    
#     def __str__(self):
#         return self.title