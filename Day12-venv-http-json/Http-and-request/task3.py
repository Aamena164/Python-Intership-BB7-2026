import requests

url=input("Enter url:")

try:
    response=requests.get(url)
    
    if response.status_code==200:
        print("Website is Online")
        
    else:
        print("Website is offline")    
        
except:
    print("Website is offline")        
        
