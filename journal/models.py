from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model() # getting the currently signed in user model

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    id_user = models.IntegerField()
    title = models.TextField(blank=True, max_length=20)
    bio = models.TextField(blank=True, max_length=100)
    profile_img = models.ImageField(upload_to='profile_images'
                                   #default='image_path' image must be in media bc that's where we specified
                                   ) 
    # ^ upload_to='' if the folder doesn't exist, it'll create one
    
    def __str__(self) -> str:
        return self.user.username
    
    
class Entry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    text = models.TextField()
    created_on = models.DateTimeField(default=datetime.now)
    last_modified_on = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField("Tag", related_name='entries')
    
    
class Tag(models.Model):
    tag_name = models.CharField(max_length=15)