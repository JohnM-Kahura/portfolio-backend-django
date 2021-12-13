from django.db import models
from django.db.models.fields import CharField

class PortfolioApp(models.Model):
    title=CharField(max_length=50)
    type=CharField(max_length=50)
    img=CharField(max_length=50)
    url=CharField(max_length=50)
    def __str__(self):
        return self.title
    
