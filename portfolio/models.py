from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=256)
    #portfolio/images will come from the media directory
    # when using ImageField you have to install pillow
    image = models.ImageField(upload_to='portfolio/images/')
    # blank=False is the default so if you want it to be okay to leave url blank you need to assign it to True
    url = models.URLField(blank=True)

    def __str__(self):
        # this is what is returned in the admin interface
        return self.title
