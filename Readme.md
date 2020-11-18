# NetMeds Web Scrapper

## Made with python

### Scrapes all the categories, medicines and medicine details from netmeds.com


# Medicine Data for a medicine from netmeds
```json
[
 {
    "id": "517119dd-9b56-4b94-b060-0539c1430645",
    "medicine_name": "Atrest 12.5mg Tablet 10'S",
    "category": {
      "id": "0853760c-ded1-4026-bb5c-3feec1904c80",
      "category": "ADHD"
    },
    "image_urls": [
      "https://www.netmeds.com/images/product-v1/150x150/851936/atrest_12_5mg_tablet_10s_0_0.jpg",
      "https://www.netmeds.com/images/product-v1/150x150/851936/atrest_12_5mg_tablet_10s_1_0.jpg",
      "https://www.netmeds.com/images/product-v1/150x150/851936/atrest_12_5mg_tablet_10s_2_0.jpg",
      "https://www.netmeds.com/images/product-v1/150x150/851936/atrest_12_5mg_tablet_10s_3_0.jpg"
    ],
    "MRP": " 154.04",
    "manufacturer": {
      "url": "https://www.netmeds.com/medicine/manufacturers/centaur-pharmaceuticals-pvt-ltd",
      "name": "Centaur Pharmaceuticals Pvt Ltd"
    },
    "Variant": "10 Tablet(s) in a Strip",
    "About": [
      "ATREST 12.5MG contains Tetrabenazine which belongs to a group of medicines called monoamine depletors",
      "It work by decreasing the amount of certain natural substances in the brain (monoamines such as dopamine, serotonin, and norepinephrine), which are involved with nerve and muscle function"
    ],
    "commonSideEffect": [
      "sleepiness (sedation)",
      "trouble sleeping",
      "depression",
      "tiredness (fatigue)",
      "anxiety",
      "restlessness",
      "agitation",
      "nausea"
    ],
    "seriousSideEffect": [
      "depression",
      "suicidal thoughts or actions",
      "neuroleptic Malignant Syndrome (NMS)",
      "high fever",
      "stiff muscles",
      "problems thinking",
      "very fast or uneven heartbeat",
      "increased sweating",
      "symptoms of Parkinsonism include: slight shaking, body stiffness, trouble moving or keeping your balance",
      "dizziness due to blood pressure changes when you change position (orthostatic hypotension)"
    ]
  }
]
```

Id for medicine and category are set manually using UUID package provided by python