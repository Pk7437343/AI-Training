#num=int(input("enter the no. of items"))
#amt=int(input("enter the input"))
#bills=[]
#for i in range(num):
#    if amt==0:
#        i=i+1
#    elif amt<0:
#        break
#    elif amt>1000:
#        bills.append(amt)
#print(bills)



while True:
    try:
        amount = float(input("Enter purchase amount: "))
        if amount < 0:
            print("Negative amount")
            break         
        if amount == 0:
            continue      
        if amount > 1000:
            print(f"Valid amount: ₹{amount}")
    finally:       
        print(" enter  amount.")


        