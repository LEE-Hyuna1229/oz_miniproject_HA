from django.shortcuts import render
from django.http import HttpResponse

def UserInfo(request):
    return HttpResponse("심리테스트!")