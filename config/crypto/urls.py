from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from crypto import views


urlpatterns = [
    path('cryptocurrencies/', views.crypto_currency),
    path("cryptocurrencies/<int:crypto_id>/", views.crypto),
]
