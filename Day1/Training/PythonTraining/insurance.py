age = int(input("Enter customer age"))
smoker = input("Smoking habit (yes/no)") == "yes"
bmi = float(input("Enter BMI"))
has_diseas = input("Severe pre-existing disease (yes/no)") == "yes"
 

if smoker and age > 50:
    decis = "High premium"
elif bmi >= 25.0:
    decis = "Medium premium"
elif has_diseas and age > 60:
    decis = "Reject"
elif age < 35 and bmi >= 18.5 and bmi < 25.0 and not smoker and not has_diseas:
    decis = "Low premium"
else:
    decis = "Std premium / Std review"
 
print("Premium decis", decis)