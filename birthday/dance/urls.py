from django.urls import URLPattern, path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    # manager
    path('trustme/jumpscare', trust, name="home"),
    path('bdaymessage', message, name="message"),
]
