from rest_framework import serializers
from .models import Work,Built

class BuiltSerializer(serializers.ModelSerializer):
    class Meta:
        model=Built
        fields=['pk','frontend','language','backend','database']

class WorkSerializer(serializers.ModelSerializer):
    built=BuiltSerializer(many=True)
    class Meta:
        model=Work
        fields=['pk','icon','title','desc','img','built']