from rest_framework import serializers
from .models import Intro,Language

class IntroSerializer (serializers.ModelSerializer):
    model=Intro
    fields=['my_image']
class LanguageSerializer (serializers.ModelSerializer):
    model=Language
    fields=['pk','language']

