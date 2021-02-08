from django.db import models
from django.db.models import NewUser
from ckeditor.fields import RichTextUploadingField

class Category(models.Model):
    CHOICES = [
        ('science & technologies','Science & Technologies'),
        ('literature','Literature'),
        ('art','Art'),
        ('logic and philosophy','Logic and Philosophy'),
        ('history','History')
    ]
    category = models.CharField(max_length=50,choices=CHOICES)

    class Meta:
        verbose_name = 'Category'

    
