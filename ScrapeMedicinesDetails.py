import json
import requests
from bs4 import BeautifulSoup
import uuid

# Scrapping medicine details from netmeds.com

with open("medicines.json", "r") as file:
    data = json.load(file)
    i = 0
    for d in data:
        i += 1
    print(i)