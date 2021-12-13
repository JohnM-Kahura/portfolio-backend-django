from django.db import models
from rest_framework import serializers
from .models import PortfolioApp

class PortfolioAppSerializer (serializers.ModelSerializer):
    class Meta:

        model=PortfolioApp
        fields=['pk','title','type','img','url']