rating = int(input("Enter rating: "))
exp = int(input("Enter experience: "))
status = input("Enter project status: ")

if rating >= 5 and exp > 10 and status == "on time":
    print("Bonus = 30%")
elif rating == 4 and exp > 7:
    print("Bonus = 20%")
elif rating == 3 and status == "delayed":
    print("Bonus = 5%")
else:
    print("Bonus = 0%")