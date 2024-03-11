import math
popA = eval(input("please enter population A: "))
popB = eval(input("please enter population B: "))
popA_per = eval(input("please enter growth rate for population A: "))
popB_per = eval(input("please enter growth rate for population B: "))
year = 0

popA_per = popA_per / 100
popB_per = popB_per / 100

while popA < popB:
    popA = popA + (popA * popA_per)
    popB = popB + (popB * popB_per)
    year+= 1

print("population A is", math.ceil(popA))
print("population B is", math.ceil(popB))
print("year is", year)