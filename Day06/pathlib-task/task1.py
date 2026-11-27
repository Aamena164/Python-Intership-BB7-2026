from pathlib import Path

folder=Path("C:/Users/ACER/OneDrive/Documents/Python-Intership-BB7-2026/Day06/pathlib-task/backup")

if folder.exists():
    print("Folder already Exists")
    
else:
    folder.mkdir()
    print("Folder created successfully")    