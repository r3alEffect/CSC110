def celsius_to_fahrenheit(celsius):
    return round(celsius*1.8+32,2)

def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit-32)*5/9,2)

print(celsius_to_fahrenheit(15))
print(fahrenheit_to_celsius(100))