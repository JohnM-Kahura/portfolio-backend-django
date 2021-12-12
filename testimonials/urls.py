from django.urls import path
from . import views

urlpatterns = [
    path("testimonials/",views.TestimonialList.as_view()),
    
]
