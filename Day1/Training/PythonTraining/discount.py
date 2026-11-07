purchaseamount=int(input("enter purchaseamountary"))
if purchaseamount==5000:
    purchaseamount= purchaseamount-0.2*purchaseamount
elif purchaseamount==2000:
    purchaseamount=purchaseamount-0.1*purchaseamount
else:
    purchaseamount=purchaseamount-0.05*purchaseamount
print(f"new purchaseamountary :: {purchaseamount}")