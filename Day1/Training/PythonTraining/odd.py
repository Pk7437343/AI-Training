c=0
codd=0
sumodd=0
for i in range(1,50):
    if i%2!=0:
        codd=codd+1
        print(f"odd number is{i}")
        sumodd=sumodd+i
print(f"sum of odd::{sumodd}")