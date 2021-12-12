from django.db import models

class Intro(models.Model):
    my_image=models.CharField( max_length=500)

class Language(models.Model):
    language= models.CharField(max_length=50)
    def __str__(self):
        return self.language
