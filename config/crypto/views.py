from django.shortcuts import render
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.http import JsonResponse
from crypto.serializers import UserSerializer
import requests
# Create your views here.
@cache_page(30)
def crypto_currency(request):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": "aad14c1c-4b0a-4257-8609-c5b1a549d329",
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return JsonResponse(data['data'], safe=False)

@cache_page(30, key_prefix="crypto")
def crypto(request, crypto_id):
    url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": "aad14c1c-4b0a-4257-8609-c5b1a549d329",
    }
    response = requests.get(url, headers=headers, params={"id": crypto_id})
    data = response.json()
    return JsonResponse(data['data'][str(crypto_id)], safe=False)


