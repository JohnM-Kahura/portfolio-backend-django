from rest_framework import generics
from .models import Work
from .serializers import WorkSerializer
class WorkList(generics.ListAPIView):
    queryset=Work.objects.all()
    serializer_class= WorkSerializer


