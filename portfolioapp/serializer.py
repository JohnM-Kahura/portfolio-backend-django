from django.db import models
from rest_framework import serializers
from .models import PortfolioApp

class PortfolioAppSerializer (serializers.ModelSerializer):
    model=PortfolioApp
    fields=['pk','title','img','url']