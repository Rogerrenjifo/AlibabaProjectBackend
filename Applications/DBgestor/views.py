from django.shortcuts import render
from django.http import HttpResponse
from Applications.DBgestor.models import Product,Search
from django.db import models
#producto1= Search.objects.create(search='bicibleta',num_of_searchs=1)
#producto1.save()
#producto1.delete()
#producto1.get
#producto= Search.objects.get(id=1)
#producto1.search=2
##leer todos los datos
#producto= Search.objects.all()
#print (producto[0].search)
def save_search(product):
    product_object= Search.objects.get_or_create(search=product)
    product_object[0].num_of_searchs +=1
    product_object[0].save()
def save_product(product):
    
    producto1= Product.objects.update_or_create(
        Title=product['Title'],
        ID_product=product['ID'],
        Score=product['Score'],
        Price=product['Price'],
        Image=product['Image'],
        Track=True,
        product='bicicleta',
        num_of_searchs=1,
        defaults={'ID_product':5},
    )
    return (producto1)
def tracker_status(request):
    product={
        'Title':'bicicleta de Rogerr',
        'ID':13,
        'Score':3.5,
        'Price':12.5,
        'Image':'//s.alicdn.com/@sc04/kf/H3e0256774a554a1193f6d8dacb57132dn.jpg_300x300.jpg',
        'product':'bicicleta'
        }
    #product, ID,product_search
    a=save_product(product)
    print (a)
    return HttpResponse("roger")
def untraked(id_product):
    product= Product.objects.get(ID_product=id_product)
    product.Track=False   
    product.save()
    