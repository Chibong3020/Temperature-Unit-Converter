import time

unit = input("The unit of the temperature ('C','F' OR 'K'): ")
temp = float(input("enter the temperature you know:" ))
unitb = input("to what unit would you like to convert the temperature ('C','F' OR 'K'): ")

if unit == 'F':
    if unitb == 'C':
        temp2 =round((temp - 32)*5/9,1)
        print(f'the temperature in celsius is {temp2}°C')
    elif unitb == 'K':
        temp3 = round((temp - 32)*5/9+273.15,1)
        print(f'the temperature in Kelvin is {temp3}°K')
elif unit == 'C':
    if unitb == 'F':
        temp4 = round(temp*9/5+32,1)
        print(f'the temperature in Fahrenheit is {temp4}°F')
    elif unitb == 'K':
        temp5 = round(temp+273.15,1)
        print(f'the temperature in Kelvin is {temp5}°K')
elif unit == 'K':
    if unitb == 'F':
        temp6 = round(temp-273.15,1)
        temp7 = round(temp6*9/5+32,1)
        print(f'the temperature in Fahrenheit is {temp7}°F')
    elif unitb == 'C':
        temp8 = round(temp-273.15,1)
        print(f'your temperature in Celsius {temp8}°C')
else:
    print("Please enter a valid unit of temperature ('C','F' OR 'K') also its caps sensitive keep that in mind and type in caps")

time.sleep(5)
    