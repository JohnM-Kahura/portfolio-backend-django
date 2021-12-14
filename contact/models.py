from django.db import models
from django.db.models.fields import CharField, TextField

class Contact(models.Model):
    name=CharField(max_length=255 ,blank=True ,null=True)
    email=CharField(max_length=255 ,blank=True ,null=True)
    message=TextField()
    def __str__(self):
        return self.email
 

