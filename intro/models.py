from django.db import models



class Language(models.Model):
    language= models.CharField(max_length=50)
    def __str__(self):
        return self.language
