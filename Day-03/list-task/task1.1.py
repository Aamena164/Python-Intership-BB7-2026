prices=[100,200,150,300,250,400,500,350,450,600]

average=sum(prices)/ len(prices)

above_average=[price for price in prices if price > average]

print("Prices:", prices)
print("Average price:", average)
print("Prices above average:", above_average)
