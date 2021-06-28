from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import


def apiOverview(request):
    return JsonResponse("API BASE POINT", safe=False)
