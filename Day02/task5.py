height_cm = "175"
weight_kg = "68.5"



height_m = float(height_cm) 
height_m=175/100
weight_kg = float(weight_kg)
BMI = weight_kg / (height_m * height_m)
print("BMI is:", BMI)