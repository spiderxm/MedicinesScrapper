import json
import requests
from bs4 import BeautifulSoup
import uuid

# Scrapping categories from netmeds.com
try:
    response = requests.get("https://www.netmeds.com/prescriptions")
    fetched_data = BeautifulSoup(response.text, "lxml")
    data = fetched_data.find_all("ul", {"class": "alpha-drug-list"})
    medicine_categories = []
    for categories in data:
        for category in categories:
            body = f"<body> {str(category)} </body>"
            d = BeautifulSoup(body, "lxml")
            medicine_category = d.get_text()
            if medicine_category != None and medicine_category != " ":
                medicine_category = medicine_category.strip()[:-4]
                if medicine_category.endswith("("):
                    medicine_category = medicine_category[:-1]
                medicine_categories.append({"id": str(uuid.uuid4()), "category": medicine_category.strip()})

    with open("categories.json", "w") as file:
        json.dump(medicine_categories, file)



except Exception as e:
    print(e)
