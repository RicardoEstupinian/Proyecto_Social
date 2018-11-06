from django.contrib import admin
from django.urls import path
from .views import periodoDirectivo

urlpatterns = [
	path('', periodoDirectivo, name="periodoDirectivo"),
]