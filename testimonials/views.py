from rest_framework import generics
from rest_framework.serializers import Serializer
from .models import Testimonial
from .serializers import TestimonialSerializer

class TestimonialList(generics.ListAPIView):
    queryset=Testimonial.objects.all()
    serializer_class=TestimonialSerializer
