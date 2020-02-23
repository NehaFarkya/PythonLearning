weight= float(input("enter your weight"))
height=float(input("enter your height"))
bmi=weight/(height**2)
print("your bmi is",round(bmi,2))

if (bmi<=18.5):
    clasification="underweight"
elif(bmi>18.5 and bmi<=24.9):
    clasification="normal weight"
elif(bmi>24.9 and bmi<=24.9):
    clasification="overweight"
else:
    clasification="Obesity"

print("The classification of your bmi is",clasification)