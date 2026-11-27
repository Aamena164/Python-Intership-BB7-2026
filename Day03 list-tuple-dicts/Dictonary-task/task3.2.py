students=[{"name":"Riya","marks":90},
         {"name":"Ananya","marks":80},
         {"name":"Rohit","marks":70}]

highest=students[0]

for student in students:
    if student["marks"]>highest["marks"]:
        highest=student
        
print("The student with the highest marks is:",highest["name"])  
print("Highest Marks:",highest["marks"])  