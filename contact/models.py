from django.db import models
from django.db.models.fields import CharField, TextField

class Contact(models.Model):
    message=TextField()
    def __str__(self):
        return 'email'
 

