annual = float(input("Enter annual income"))
age = int(input("Enter age"))
invest = float(input("Enter investment amount"))
 
taxinco = annual - invest
 
if age >= 60:
    taxinco = taxinco-50000 
if taxinco < 0:
    taxinco = 0 
if taxinco < 500000:
    tax = 0
elif taxinco <= 1000000:
    tax = taxinco * 0.10
elif taxinco <= 2000000:
    tax = taxinco * 0.20
else:
    tax = taxinco * 0.30
print("Calculated Tax---", tax)