def farenheit(celsius):
    return celsius*(9/5) + 32

temp_outdoors = int(input("How many degrees Celsius is it outside? "))
converted_temp = farenheit(temp_outdoors)
print(f"It is {converted_temp} degrees in Farenheit right now.")