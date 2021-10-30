from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('judge/', include('judge.urls')),
    path('admin/', admin.site.urls),
]
