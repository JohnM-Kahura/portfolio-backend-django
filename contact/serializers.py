from django.db import models
from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
   class Meta:
        model=Contact
        fields=['pk','name','email','message']