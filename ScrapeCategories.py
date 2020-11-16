import requests
from bs4 import BeautifulSoup

try:
    response = requests.get("https://www.netmeds.com/prescriptions")
    data = BeautifulSoup(response.text , "lxml")
    categories = data.find("ul", {"class" : "alpha-drug-list"})
    print(len(categories))

except Exception as e:
    print(e)

