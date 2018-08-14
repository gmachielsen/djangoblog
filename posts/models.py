from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



# Create your models here.
class Post(models.Model):
    PAINTING_TYPE_CHOICES = (
        ('L', 'Landscape'),
        ('P', 'Portrait'),
        ('A', 'Animals'),
        ('S', 'Still Life'),
    )
    
    MEDIUM_CHOICES = (
        ('O', 'Oil'),
        ('A', 'Acrylic'),
        ('W', 'Watercolour'),
        ('C', 'Charcoal'),
    )
    
    LEVEL_CHOICES = (
        ('B', 'Beginner'),
        ('A', 'Advanced'),
        ('N', 'N/A'),
    )
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    author = models.ForeignKey(User, related_name='posts', null=False, default=1, on_delete=models.SET_DEFAULT) 
    image = models.ImageField(upload_to="images", null=True, blank=True)
    painting_type = models.CharField(max_length=1, default= "L", choices=PAINTING_TYPE_CHOICES)
    medium = models.CharField(max_length=1, default= "O", choices=MEDIUM_CHOICES)
    level = models.CharField(max_length=1, default= "B", choices=LEVEL_CHOICES)
    
    
    
    def __str__(self):
        return self.title
