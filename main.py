#script to  read and print out names and prices.


import json

file = "cars.json"

with open (file, "r") as json_file:
    data = json.load(json_file)
    car_data = (data["cars"])
    for i in car_data:
        brand = (i["brand"])
        price = (i["price"])
        print (f"{brand} costs ${price}")


