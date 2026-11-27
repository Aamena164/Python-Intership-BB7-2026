f=open("C:/Users/ACER/OneDrive/Documents/Python-Intership-BB7-2026/Day06/File/my_story.txt","a")

f.write("\nDate:2026-07-22")
f.close()

f=open("C:/Users/ACER/OneDrive/Documents/Python-Intership-BB7-2026/Day06/File/my_story.txt","r")

data=f.read()
print(data)