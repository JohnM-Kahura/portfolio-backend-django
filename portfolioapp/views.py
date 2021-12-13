from rest_framework import generics
from .models import PortfolioApp
from .serializer import PortfolioAppSerializer

class PortFolioList(generics.ListAPIView):
    queryset=PortfolioApp.objects.all()
    serializer_class=PortfolioAppSerializer