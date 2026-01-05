### weight converter
weight = float(input("enter your weight:   "))
unit=input("enter your unit (K or L) :   ")


if unit=="K":
    weight=weight*2.205
    unit="lbs"
    print(f"your weight is:  {round (weight,1)} {unit}")
elif unit=="L":
    weight = weight /2.265
    unit ="kgs"
    print(f"your weight is:  {round(weight, 1)} {unit}")
else :
    print(f"sorry i dont understand that")
