
import os
import json
import requests 

base_url="https://api.covid19api.com/"

def base():

    req = requests.get(base_url)
    print(req.text)

def get_day_one():
    url="{}dayone/country/south-africa/status/confirmed".format(base_url)
    req = requests.get(url)
    return req.text

if __name__ == "__main__":
    print (get_day_one())
