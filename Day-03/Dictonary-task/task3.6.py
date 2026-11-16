employees={
    "Alexa":40000,
    "Seema":50000,
    "Neha":600000,
    "Suresh":70000,
    "Riya":670000
}

sorted_employees=sorted(
    employees.items(),
    key=lambda x:x[1],
    reverse=True
)

for name , salary in sorted_employees[:3]:
    print(name,":",salary)