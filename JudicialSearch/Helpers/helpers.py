import requests
import os
import json

def get_page_data(url):
    
    response = requests.get(url)
    response_json = response.json()
    return response_json


from urllib.parse import urlparse


def get_data_search():

    url = "https://www.buscadorambiental.cl/buscador-api/jurisprudencias/list" 

    payload = {
        "page": 1,
        "pageSize": 100,
        "search": " ",
        "orden": "nuevo"
    }

    
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response
