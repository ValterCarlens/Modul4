import os
import random
os.system('cls')

 #  Upg 1

"""
a = 160

längd = (int(input("Hur lång är du? ")))

if längd < a :
    print("du är för kort" )
else:
    print("Du kan åka")

"""

# upg 2
""""
namn = input("Hej vad heter du? ")

print ("hej " + namn )

ålder = (str(input("hur gammal är du? ")))

print ("okej du är " + ålder)
"""

# upg 3

"""
vikt = float( input("Ange din vikt (kg): "))
längd = float(input("Ange din längd (m): "))

bmi = vikt/längd**2

print(f"Ditt BMI är {bmi}")

"""
# upg 4 beräkna area på cirkel


import math 

"""
x = math.pi

print(x)

radie=(float(input("vad är radien")))

arean = x * radie**2

print(arean)
"""

 #Upg 5

"""
print("1 = +\n 2 = -\n 3 = /\n 4 = *")
val = int(input("Vilket räknesätt? "))

if val == 1:
    x = int(input("ange första tal "))
    y = int(input("ange andra tal "))
    additiontal = x + y
    print (additiontal)

elif val == 2:
    x = int(input("ange första tal "))
    y = int(input("ange andra tal "))
    subtraktiontal = x - y
    print(subtraktiontal)

elif val == 3:
    x = int(input("ange första tal "))
    y = int(input("ange andra tal "))
    divisiontal = x / y
    print(divisiontal)

elif val == 4:
    x = int(input("ange första tal"))
    y = int(input("ange andra tal"))
    multiplikationstal = x * y
    print(multiplikationstal)


"""

#upg 6

"""
print(random.randint(1, 6))

"""
# upg 7

"""
tärningar = int(input("hår många tärningar vill du kasta? "))


for x in range ( tärningar ):
    tärningkast = random.randint(1, 6)
    print(f"resultatet av tärning {x + 1}:  {tärningkast}")

"""