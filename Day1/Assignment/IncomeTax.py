income = float(input("Enter income: "))
age = int(input("Enter age: "))

if age >= 60:
    print("Senior Citizen Exemption")
elif income < 500000:
    print("Tax = 0")
elif income < 1000000:
    print(f"Tax = {income*0.1}")
elif income < 2000000:
    print(f"Tax = {income*0.2}")
else:
    print(f"Tax = {income*0.3}")