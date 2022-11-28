"""views of Backend"""
import requests
from django.http.response import JsonResponse
#from django.shortcuts import render
from .views_function import *
from Applications.DBgestor.views import save_search
def backend(request,product):
    """this function is the orchestrator"""
    url=assemble_url(product)
    save_search(product)
    data_from_url=web_scraper(url)
    search_results=parcer(data_from_url)
    ordered_products=sorf_list(search_results)
    #print (request.method)
    #print (product)
    #print (type(ordered_products))
    return JsonResponse(ordered_products,safe=False)
