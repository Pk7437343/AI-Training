sal=int(input("enter salary"))
if sal>=50000:
    sal= sal+0.2*sal
elif sal>30000 & sal<50000:
    sal=sal+0.1*sal
elif sal<30000:
    sal=sal+0.05*sal
print(f"new salary :: {sal}")