with open("input.txt","r") as f:
        
 data=f.read()

 print(data)
 print("Total number of words:",len(data.split()))