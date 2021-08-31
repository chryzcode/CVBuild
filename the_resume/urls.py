from django.urls import path
from .views import resume

urlpatterns = [
    path('', resume, name='resume'),
]