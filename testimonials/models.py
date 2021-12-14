from django.db import models

class Testimonial(models.Model):
    name=models.CharField( max_length=50)
    title=models.CharField( max_length=50)
    img=models.CharField( max_length=500)
    icon=models.CharField( max_length=50)
    desc=models.CharField( max_length=50)
    social=models.CharField( max_length=50)
    featured=models.BooleanField()
    def __str__(self):
        return self.name
