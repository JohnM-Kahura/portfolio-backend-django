from django.urls import path
from . import views

urlpatterns = [
    path("work/",views.WorkList.as_view()),
    
]