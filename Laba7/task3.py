import json

with open("ex_3.json") as f:
    data = json.load(f)

data["invoices"].append(
    {
      "id": 3,
      "total": 4242.00,
      "items": [
        {
          "name": "item 4",
          "quantity": 101,
          "price": 42.00
        }
      ]
    }
)

with open("ex_3_new.json", "w+") as f:
    json.dump(data, f)