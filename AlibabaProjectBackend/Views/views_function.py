"""this part has the function of the VIEWS"""
import json
import requests
from bs4 import BeautifulSoup
def assemble_url(search):
    """Assemble the url with the product to search for"""
    url = f'https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&tab=all&SearchText={search}'
    return url
def web_scraper(url):
    """Get de info from url"""
    result = requests.get(url)
    soup = BeautifulSoup(result.content, 'html.parser')
    json_result = soup.findAll('script')[36].text.strip()[30:-64]
    format_json = json.loads(json_result)
    data_from_url = format_json['props']['offerResultData']['offerList']
    return (data_from_url)
def parcer(data_from_url):
    """filter useful data on a list of dictionaries"""
    search_results =[]
    for i in data_from_url:
        search_results.append({
            'Title':i['information']['puretitle'],
            'ID':i['id'],
            'Score':float(i['reviews'].get('productScore',0)),
            'Price':(i['promotionInfoVO']['localOriginalPriceFromStr'][1:]),
            'Image':i['image']['mainImage']
        })  
    data_json =json.dumps(search_results) #json
    return (search_results)
def sorf_list(list_of_data):
    """order the info by price and score"""
    return list_of_data
