from django.db import models

class Work(models.Model):
    icon=models.CharField( max_length=255)
    title=models.CharField( max_length=255)
    desc=models.CharField( max_length=255)
    img=models.CharField( max_length=255)
    def __str__(self):
        return self.title

