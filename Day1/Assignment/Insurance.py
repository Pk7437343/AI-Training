age = int(input("Enter age: "))
bmi = float(input("Enter BMI: "))
disease = input("Disease (Y/N): ")

if age > 60 and disease == "Y":
    print("Reject")
elif age > 50:
    print("High Premium")
elif 25 <= bmi <= 29.9:
    print("Medium Premium")
elif disease == "N":
    print("Low Premium")
