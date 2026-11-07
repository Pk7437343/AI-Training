wt=int(input("enter weight"))
ht=int(input("enter height"))
bmi=wt/(ht**2)
if bmi<18.5:
    print("underweight")
elif bmi>18.5 & bmi<24.9:
    print("normal")
elif bmi>25 & bmi<29.9:
    print("overweight")
elif bmi>30:
    print("obese")
