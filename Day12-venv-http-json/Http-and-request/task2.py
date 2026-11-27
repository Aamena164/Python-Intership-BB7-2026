import requests

url="https://httpbin.org/status/404"

response=requests.get(url)

print("Status code:",response.status_code)

if response.status_code==200:
    print("Request Successfull")
elif response.status_code==404:
    print("Error:Page Not found")    
else:
    print("Something went wrong")    