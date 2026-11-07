hours = int(input("Enter hours: "))
storage = int(input("Enter storage: "))
plan = input("Enter plan: ")

if plan == "Basic":
    bill = hours*10 + storage*2 + 500
elif plan == "Premium":
    bill = hours*8 + storage*2 + 1500
elif plan == "Enterprise":
    bill = hours*5 + storage*1.5 + 5000
else:
    bill = 0

print("Bill =", bill)