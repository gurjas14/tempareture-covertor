#change this value for a different result
#celsius = 37.5
celsius = float(input("Please enter the temperature in celsius:"))



#calculate fharenheit
fharenheit = (celsius * 1.8) + 32
print('%0.1f degree celsius is equal to %0.1f degree fahrenheit' %(celsius,fharenheit))


temp = fharenheit

if (temp >= 104):
  print("It is hot")
elif (temp <=50):
    print("It is cold") 
else:
    print("The temperature is nice")      