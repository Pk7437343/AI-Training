import pandas as pd


salary_series = pd.Series([65000, 58000, 80000, 85000, 68000, 90000, 76000])
print(salary_series)

# print(salary_series.index)
# print(salary_series.value)
# print(salary_series.dtype)


employee_series = pd.Series(
    [
        "Shiv","Atharva","hitesh", "prince",
        "akash", "pranjali", "shreyans", "sahil"
    ],
    index=[
        "E101", "E102", "E103", "E104",
        "E105","E106","E107","E108"
        ]
)
print(employee_series)

#retrieve employees
print(employee_series["E103"])
print(employee_series["E106"])

employee_data={
    "Employee_ID": ["E101", "E102", "E103","E104","E105","E106","E107","E108"],
    "Employee_Name": ["Amit Sharma", "Neha Verma", "Rahul Singh", "Priya Gupta", "Karan Mehta", "Anjali Mehta",
                      "Mohit Jain", "Sneha Kapoor"],
    "Department": ["Sales", "HR", "Sales", "Finance", "IT", "Sales", "IT", "Finance"],
    "City": ["Delhi", "Mumbai", "Pune", "Delhi", "Mumbai", "Bengaluru", "Pune", "Delhi"],
    "Salary": [65000, 58000,72000,80000,85000,68000,90000,76000],
    "Experience": [5,4,7,8,6,5,9,6],
    "Rating": [4.5,4.2,4.8,4.6,4.1,4.7,4.9,4.3]
}
print("employee dataframe")
employee_df = pd.DataFrame(employee_data)

res=employee_df[
    employee_df["Salary"]>80000
]
print(res)

resu=employee_df[
    employee_df["Rating"]>4.5
]
print(resu)

print(employee_df[
    employee_df["Department"]=="Sales"
])

result_dept_sales=(employee_df[
    employee_df["Department"]=="Sales"
])
result_dept_sales

result_city_delhi=employee_df[
    employee_df["City"]=="Delhi"
]
print(result_city_delhi)

result_salary_rating= employee_df[
    (employee_df["Rating"]>4.5) &
    (employee_df["Salary"]>70000)
]
print(result_salary_rating)

result_dept_name= employee_df[
    (employee_df["Department"]=="IT") &
    (employee_df["Department"]=="Finance")
]
print(result_dept_name)

result_dept_names= employee_df[
    employee_df["Department"].isin(["IT","Finance"])
  
]
print(result_dept_names)

employee_df["annual salary"]=  employee_df["Salary"]*12
print(employee_df)



employee_df["revised salary"]=  employee_df["Salary"]*0.08
print(employee_df)

employee_df["PerformanceBonus"]=  employee_df["revised salary"]*0.1
print(employee_df)

employee_df["Monthly compensation"]= employee_df["revised salary"]+employee_df["PerformanceBonus"]
print(employee_df)

Average_salary = employee_df["revised salary"].mean()
print(Average_salary)

Sum_of_salary = employee_df["revised salary"].sum()
print(Sum_of_salary)

Minimum_salary = employee_df["revised salary"].min()
print(Minimum_salary)

Maximum_salary = employee_df["revised salary"].max()
print(Maximum_salary)

Average_Rating = employee_df["Rating"].mean()
print(f"Average::{Average_Rating}")

department_count= employee_df["Department"].value_counts()
print(department_count)

length=len(employee_df["Department"]=="IT")
print(length)

department_unique= employee_df["Department"].nunique()
print(department_unique)

department_sorting = employee_df.sort_values("Salary")["Department"]
print(department_sorting)

department_desc = employee_df.sort_values(by="Salary", ascending=False)
print(department_desc)

department_top3 = employee_df.sort_values(by="Salary", ascending=False).head(3)
print(department_top3)