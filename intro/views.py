from rest_framework import generics
from .models import Language
from .serializers import  LanguageSerializer

class IntroList(generics.ListAPIView):
    queryset=Language.objects.all()
    serializer_class=LanguageSerializer