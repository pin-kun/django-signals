from django.urls import path
from clientip.views import *

urlpatterns = [
    path('', home, name='home-page')
]
