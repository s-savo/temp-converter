temp=input("temp in degrees")
if temp.lower=="q":
    print("Goodbye!!")
else:
    celcius=float(temp)
    fahrenheit=celcius*9/5+32
    print(f"{celcius} degrees celcius is {fahrenheit} degrees fahrenheit")
    print("arigato gozaimasu!!")
