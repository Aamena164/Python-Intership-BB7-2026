from pathlib import Path

file=Path("C:/Users/ACER/OneDrive/Documents/Python-Intership-BB7-2026/Day06/pathlib-task/notes.txt")

if not file.exists():
    file.touch()
    print("File created") 
    
print("File size:",file.stat().st_size,"bytes") 
print("File suffix:",file.suffix)   

