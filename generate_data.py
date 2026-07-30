import pandas as pd
import random
from datetime import datetime, timedelta

# Cities
cities = [
    "Delhi",
    "Mumbai",
    "Bengaluru",
    "Hyderabad",
    "Chennai",
    "Pune"
]

# Salespersons
salespersons = [
    "Amit",
    "Neha",
    "Rahul",
    "Priya",
    "Arjun",
    "Sneha",
    "Karan",
    "Anjali"
]

# Products
products = {
    "Electronics": [
        ("Laptop",65000),
        ("Mobile",32000),
        ("Headphones",4500),
        ("Tablet",25000),
        ("Monitor",15000),
        ("Smart Watch",12000)
    ],

    "Furniture":[
        ("Office Chair",7500),
        ("Study Table",6500),
        ("Bookshelf",8500),
        ("Sofa",35000),
        ("Wardrobe",18000)
    ],

    "Grocery":[
        ("Rice",1200),
        ("Tea",600),
        ("Coffee",900),
        ("Sugar",700),
        ("Cooking Oil",1800)
    ],

    "Clothing":[
        ("T-Shirt",1200),
        ("Jeans",2200),
        ("Shoes",3500),
        ("Jacket",4500),
        ("Kurta",1800)
    ],

    "Home Appliances":[
        ("Microwave",9500),
        ("Mixer Grinder",4200),
        ("Air Fryer",7000),
        ("Vacuum Cleaner",11000),
        ("Electric Kettle",1800)
    ]
}

data = []

start_date = datetime(2025,1,1)

for order in range(1001,1351):

    category = random.choice(list(products.keys()))

    item, price = random.choice(products[category])

    discount = random.randint(50,3000)

    sold = random.randint(1,15)

    city = random.choice(cities)

    person = random.choice(salespersons)

    date = start_date + timedelta(days=random.randint(0,180))

    data.append({

        "Order_ID":order,

        "Date":date.strftime("%d-%m-%Y"),

        "City":city,

        "Category":category,

        "Item":item,

        "Price":price,

        "Discount":discount,

        "Sold_Unit":sold,

        "Salesperson":person

    })

df = pd.DataFrame(data)

df.to_excel("sales.xlsx",index=False)

print("Excel File Created Successfully!")