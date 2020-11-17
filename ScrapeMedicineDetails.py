import json
import requests
from bs4 import BeautifulSoup
import uuid

# Scrapping medicine details from netmeds.com
try:
    with open("medicine.json", "w") as file1:
        with open("medicines.json", "r") as file:
            data = json.load(file)
            Medicines = []
            for medicine in data:
                name = medicine["medicine_name"]
                Medicine = medicine
                name = name.lower().replace(' ', '-').replace('\'', '-').replace("\\", "-").replace(".", "-")
                name = name.replace("%", "")
                first = name.find("(")
                last = name.find(")")
                if first != -1:
                    name = name.replace(name[first: last + 1], "")
                print(name)
                url = "https://www.netmeds.com/prescriptions/" + name
                data = requests.get(url)
                if data.status_code == 200:
                    Data = BeautifulSoup(data.text, "lxml")
                    images = Data.find("div", {"class": "swiper-wrapper"})
                    # Taking image urls
                    image_urls = []
                    for image in images:
                        data = BeautifulSoup(f" <body> f{image} </body>", "lxml")
                        i = data.find('img', {})
                        if i is not None:
                            image_urls.append(i['src'])
                    Medicine["image_urls"] = image_urls
                    # Finding Out MRP
                    amount = Data.find("span", {"class": "final-price"}).get_text().replace("M.R.P.: Rs.", "")
                    print(amount)
                    break




except Exception as e:
    print(e)
