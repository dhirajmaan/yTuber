from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.


class Youtubers(models.Model):

    crew_choices = (

        ('solo', 'solo'),
        ('small', 'small'),
        ('large', 'large'),
    )
    camera_choices = (
        ('Cannon', 'Cannon'),
        ('Nikon', 'Nikon'),
        ('Sony', 'Sony'),
        ('Red', 'Red'),
        ('sony', 'sony'),
        ('Panasonic', 'Panasonic'),
        ('Fuji', 'Fuji'),
        ('Others', 'Others'),
    )
    category_choices = (
        ('Code', 'Code'),
        ('Mobile_review', 'Mobile_review'),
        ('Vlog', 'Vlog'),
        ('Gaming', 'Gaming'),
        ('Flim_making', 'Flim_making'),
        ('Cooking', 'Cooking'),
    )

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='meadia/ytubers/%y/%M')
    video_url = models.CharField(max_length=255)
    description = RichTextField()
    city = models.CharField(max_length=255)
    age = models.IntegerField()
    height = models.IntegerField()
    crew = models.CharField(choices=crew_choices, max_length=255)
    camera_type = models.CharField(choices=camera_choices, max_length=255)
    subs_count = models.CharField(max_length=255)
    category = models.CharField(choices=category_choices, max_length=255)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
