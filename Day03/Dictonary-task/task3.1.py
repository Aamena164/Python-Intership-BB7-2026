product={
    "Bag": 1000,
    "Calculator":500,
    "Phone":150,
    "pen":10,
    "pencil":5
}

print("product grater price than 100:")
for key, value in product.items():
    if value > 100:
        print(key, ":", value)