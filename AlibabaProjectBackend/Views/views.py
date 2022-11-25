#import requests 
#import json
#import pandas as pd
from django.views import View
from django.http.response import HttpResponse
from django.shortcuts import render

def backend(request):
    list_of_backend=[{'name':'Alibaba','num':'1'},{'name':'No Alibaba','num':'2'}]
    return HttpResponse(list_of_backend)  
