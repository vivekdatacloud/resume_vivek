
from django.contrib import admin
from django.urls import path
from prime.views import *
from django.conf import settings
from django.conf.urls.static import static
from prime import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('contactform/',views.save_form,name='contactform'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)