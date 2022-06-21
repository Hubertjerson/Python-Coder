from django.urls import path
from .views import  family

urlpatterns = [
    path('', family ),
]
