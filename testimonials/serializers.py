from django.db.models import fields
from rest_framework import serializers
from .models import Testimonial
class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model= Testimonial
        fields=['pk','name','title','img','icon','desc','social','featured']
