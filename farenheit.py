def celsius(farenheit):
    return ((farenheit-32)*(5/9))

temp_in_celsius = int(input("What temperature is it in Farenheit outside? "))
temp_converted = celsius(temp_in_celsius)
print(f"It is {temp_converted:.2f} degrees Celsius out there!")