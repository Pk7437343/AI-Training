monsal = float(input("Enter monthly salary"))
cscore = int(input("Enter credit score"))
loan = float(input("Enter loan amount"))
emptype= input("Enter employment type: ")
 
if monsal > 80000 and cscore > 750 and loan < 20000:
    print("Approve Immediately")
elif monsal > 50000 and cscore > 650:
    print("Approve with caution")
elif cscore < 600:
    print("Reject")
else:
    print("Put under manual review")