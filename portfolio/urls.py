from django.contrib import admin
from django.urls import path,include



urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include("testimonials.urls"),name='testimonials'),
    path('', include("intro.urls"),name='intro'),
    path('', include("portfolioapp.urls"),name='portfolio'),
    path('', include("work.urls"),name='work'),
    path('', include("contact.urls"),name='contact'),
]
