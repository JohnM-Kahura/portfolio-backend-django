from django.urls import path
from . import views
urlpatterns = [
    path("portfolio/",views.PortFolioList.as_view()),
]
