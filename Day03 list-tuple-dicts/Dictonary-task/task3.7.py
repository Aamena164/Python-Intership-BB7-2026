stock={
    "Pen":10,
    "Book":5,
    "Pencil":8
}

stock["Pen"]=stock["Pen"]+5

item="Book"

if item in stock:
    stock[item]=stock[item]-1
    print("Item sold successfully")
else:
    print("Product not found")    
    
print("Available stock:",stock)    