import requests
from bs4 import BeautifulSoup

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
                medicine_categories.append(medicine_category.strip())
    print(medicine_categories)



except Exception as e:
    print(e)
