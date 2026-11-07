
sentence = input("Enter a sentenc: ")
vowc = 0
conc = 0
vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
for ch in sentence:
    if ch == " ":
        continue
    if ch == "!":
        break   
    if ch in vowels:
        vowc += 1
    elif ch in consonants:
        conc += 1
print(f"Total vowels: {vowc}")
print(f"Total consonants: {conc}")