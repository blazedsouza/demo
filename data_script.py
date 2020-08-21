
import os
import json
import requests 

base_url="https://api.covid19api.com/"

def base():

    req = requests.get(base_url)
    print(req.text)

if __name__ == "__main__":
    print (base())
