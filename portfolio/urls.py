from django.contrib import admin
from django.urls import path,include
from django.conf import settings    
from django.conf.urls.static import static


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include("testimonials.urls"),name='testimonials'),
    path('', include("intro.urls"),name='intro'),
    path('', include("portfolioapp.urls"),name='portfolio'),
    path('', include("work.urls"),name='work'),
    path('', include("contact.urls"),name='contact'),
]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

