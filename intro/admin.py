from django.contrib import admin
from .models import Intro,Language
mymodels=[Intro,Language]
admin.site.register(mymodels)
