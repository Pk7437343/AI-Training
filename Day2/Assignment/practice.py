# import keyword
# print(keyword.kwlist)

# #strings

# s=input("enter the string")
# print(s)

# a= "Aman"
# print(a.upper())
# print(a.lower())

# b= "  dehradun  "
# print(b.strip())







# from abc import ABC, abstractmethod

# # Inheritance
# class Animal:
#     def sound(self):
#         print("Animal makes sound")

# class Dog(Animal):
#     species = "Canine"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def sound(self):
#         print("Dog Barks")

# # Encapsulation
# class Employee:
#     def __init__(self, salary):
#         self.__salary = salary

#     def show_salary(self):
#         print("Salary =", self.__salary)

# # Abstraction
# class Vehicle(ABC):

#     @abstractmethod
#     def start(self):
#         pass

# class Car(Vehicle):

#     def start(self):
#         print("Car Started")

# # Operator Overloading
# class Number:

#     def __init__(self, num):
#         self.num = num

#     def __add__(self, other):
#         return self.num + other.num


# while True:

#     print("\n===== OOP MENU =====")
#     print("1. Create Object")
#     print("2. Inheritance")
#     print("3. Polymorphism")
#     print("4. Encapsulation")
#     print("5. Abstraction")
#     print("6. Class Variable")
#     print("7. Operator Overloading")
#     print("8. Exit")

#     ch = int(input("Enter Choice: "))

#     if ch == 1:
#         d = Dog("Buddy", 3)
#         print("Name:", d.name)
#         print("Age:", d.age)

#     elif ch == 2:
#         d = Dog("Tom", 2)
#         d.sound()

#     elif ch == 3:
#         d = Dog("Rocky", 4)
#         d.sound()

#     elif ch == 4:
#         e = Employee(50000)
#         e.show_salary()

#     elif ch == 5:
#         c = Car()
#         c.start()

#     elif ch == 6:
#         print("Species =", Dog.species)

#     elif ch == 7:
#         n1 = Number(10)
#         n2 = Number(20)
#         print("Addition =", n1 + n2)

#     elif ch == 8:
#         print("Program Ended")
#         break

#     else:
#         print("Invalid Choice")


import numpy as np
import pandas as pd

df = pd.read_csv("HSBC_Synthetic_Banking_Customers.csv")
salary =np.array(df.Account_Balance)
print("salary above 5000", salary[salary>50000])

# print("mean", np.mean(salary))
# print("mean", np.mean(df["Account_Balance"]))
# print("mean", df["Account_Balance"].mean())
# print("mean", df.Account_Balance.mean())

# print("std deviation", np.std(salary))
# print("std", df.Account_Balance.std())



# #Calculate sum, mean, median and standard deviation of balances. 
# print("sum of balances", salary.sum())
# print("mean of balance : ", salary.mean())
# print("mean of balance : ", np.mean(salary))
# print("median balance", np.median(salary))
# print("standard deviation", salary.std())

# percentile = np.percentile(salary, [25,50,45])
# print(percentile)

# data = np.column_stack((
#     salary,
#     df['Monthly_Deposit'],
#     df['Monthly_Withdrawal']
# ))
 
# print(data)
 
# print(np.sum(data, axis=0))
# print(np.sum(data, axis=1))

# correlation = np.corrcoef(
#     df['Monthly_Income'],
#     df['Account_Balance']
# )
 
# print(correlation)

# 22. Display first and last ten rows. 
print(df.head(10))
print(df.tail(10))


print(df.info)

# print("database shape", df.shape)
# print("database size", df.size)
# print("colums", df.columns)
# print("dtype", df.dtypes)

# print("describe" , df.describe())

# print("duplicate ",df["Account_Balance"].duplicated().sum())
# print("null check", df["Account_Balance"].isnull())

result_age = df[df["Age"]>=25]
print(result_age)

print(df["Monthly_Deposit"])