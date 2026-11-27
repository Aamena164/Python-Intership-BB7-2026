with open("input.txt","r") as f:
    data=f.read()
    print(data)
    
with open("copy.txt","w") as f:
    f.write(data)
    
print("Program copied succesfully")        
    