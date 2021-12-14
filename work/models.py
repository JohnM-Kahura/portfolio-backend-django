from django.db import models
def upload_to(instance,filename):
    return 'work/{filename}'.format(filename=filename)
    
class Work(models.Model):
    icon=models.CharField( max_length=255)
    title=models.CharField( max_length=255)
    desc=models.CharField( max_length=255)
    img=models.ImageField(('Image'),upload_to=upload_to,default='work/default.jpeg')
    def __str__(self):
        return self.title


class Built(models.Model):
    language=models.CharField(max_length=50,blank=True)
    frontend=models.CharField(max_length=50,blank=True)
    backend=models.CharField(max_length=50,blank=True)
    database=models.CharField(max_length=50,blank=True)
    work=models.ForeignKey(Work,on_delete=models.CASCADE,related_name='built')

    def __str__(self):
        return self.language

