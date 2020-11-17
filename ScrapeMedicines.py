import json
import requests
from bs4 import BeautifulSoup
import uuid

# Scrapping medicine names from netmeds.com


try:
    with open("medicines.json", "w") as file1:
        with open("categories.json", "r") as file:
            data = json.load(file)
            Medicines = []
            for category in data:
                url = "https://www.netmeds.com/prescriptions/" + category["category"].lower().replace(' ', '-').replace(
                    '/',
                    '-')
                response = requests.get(url)
                fetched_data = BeautifulSoup(response.text, "lxml")

                medicines = fetched_data.find_all("li", {"class": "product-item"})
                for medicine in medicines:
                    body = f"<body> {str(medicine)} </body>"
                    name = BeautifulSoup(body, "lxml").get_text()
                    Medicines.append({
                        "id": str(uuid.uuid4()),
                        "medicine_name": name.strip(),
                        "category": category
                    })
        json.dump(Medicines, file1)

except Exception as e:
    print(e)
