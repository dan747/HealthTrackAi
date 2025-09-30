from django.contrib import admin
from django.urls import path, include
from . import views   # 👈 so we can add a homepage

urlpatterns = [
    path('', views.home, name='home'),       # homepage
    path('admin/', admin.site.urls),
    path('patients/', include('patients.urls')),  # 👈 link to patients app
]
