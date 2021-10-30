from django.urls import path
from .views import prob_list

urlpatterns = [
    path('', prob_list)
]
