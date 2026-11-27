prod_rec=("car",50000,2)
print("Original product record:", prod_rec)

#Trying to change price of first tuple
#prod_rec[1]=("car", 55000, 2)
#print(prod_rec)

#TypeError: 'tuple' object does not support item assignment
#tuples are immutable meaning that once they are created, their elements cannot be changed or modified. 

#Creating new tuple with updated price
prod_rec=("car",55000,2)
print("Updated product record:", prod_rec)