import json
import requests
from bs4 import BeautifulSoup
import uuid

Medicines = []
# Scrapping medicine details from netmeds.com
with open("medicine.json", "w") as file1:
    try:
        with open("medicines.json", "r") as file:
            data = json.load(file)
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
                    if images is not None:
                        for image in images:
                            data = BeautifulSoup(f" <body> f{image} </body>", "lxml")
                            i = data.find('img', {})
                            if i is not None:
                                image_urls.append(i['src'])
                    Medicine["image_urls"] = image_urls
                    # Finding Out MRP
                    amount = Data.find("span", {"class": "final-price"}).get_text().replace("M.R.P.: Rs.", "")
                    Medicine["MRP"] = amount

                    # Finding Manufacturer
                    manufacturerData = Data.find("span", {"class": "drug-manu"})
                    manufacturerData = manufacturerData.find("a", {})
                    manufacturer_url = manufacturerData['href']
                    manufacturer_name = manufacturerData.get_text()
                    manufacturer = {
                        "url": manufacturer_url,
                        "name": manufacturer_name
                    }
                    Medicine["manufacturer"] = manufacturer

                    # Variant
                    try:
                        Variant = Data.find("span", {"class": "drug-varient"}).get_text()
                        Medicine["Variant"] = Variant
                    except:
                        Medicine["Variant"] = None

                    # About Medicine
                    about = []
                    try:
                        AboutData = Data.find("div", {"class": "druginfo-dv"}).find("ul", {}).find_all("li", {})
                    except:
                        AboutData = None
                    if AboutData is not None:
                        for info in AboutData:
                            info = str(info)
                            info = info.replace("<li>", "").replace("</li>", "")
                            about.append(info)
                    Medicine["About"] = about

                    # CommonSideEffects
                    commonSideEffects = []
                    try:
                        CommonSideEffectsData = Data.find("div", {"id": "common-side-effects"}).find("ul").find_all(
                            "li")
                    except:
                        CommonSideEffectsData = None
                    if CommonSideEffectsData is not None:
                        for commonSideEffect in CommonSideEffectsData:
                            commonSideEffect = str(commonSideEffect)
                            commonSideEffect = commonSideEffect.replace("<li>", "").replace("</li>", "")
                            commonSideEffects.append(commonSideEffect)
                    Medicine["commonSideEffect"] = commonSideEffects
                    # SeriousSideEffects
                    seriousSideEffects = []
                    try:
                        SeriousSideEffectsData = Data.find("div", {"id": "serious-side-effects"}).find("ul").find_all(
                            "li")
                    except:
                        CommonSideEffectsData = None
                    if SeriousSideEffectsData is not None:
                        for seriousSideEffect in SeriousSideEffectsData:
                            seriousSideEffect = str(seriousSideEffect)
                            seriousSideEffect = seriousSideEffect.replace("<li>", "").replace("</li>", "")
                            seriousSideEffects.append(seriousSideEffect)
                    Medicine["seriousSideEffect"] = seriousSideEffects
                    Medicines.append(Medicine)
    except Exception as e:
        print(e)

    json.dumps(Medicines, file1)
