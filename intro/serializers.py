from rest_framework import serializers
from .models import Language

class LanguageSerializer (serializers.ModelSerializer):
    model=Language
    fields=['pk','language']

