import pandas as pd
import numpy as np
employee_data={
    "Employee_ID": ["E101", "E102", "E103","E104","E105","E106","E107","E108"],
    "Employee_Name":  [
            "Shiv","Atharva","hitesh", "prince",
            "akash", "pranjali", "shreyans", "sahil"
        ],
    "Department": ["Sales", "HR", "Sales", "Finances", "IT", "Sales", "IT", "Finance"],
    "City": ["Delhi", "Mumbai", "Pune", "Delhi", "Mumbai", "Bengaluru", "Pune", "Delhi"],
    "Salary": [65000, 58000,72000,80000,85000,68000,90000,76000],
    "Experience": [5,4,7,8,6,5,9,6],
    "Rating": [4.5,4.2,4.8,4.6,4.1,4.7,4.9,4.3]
}
print("employee dataframe")
employee_df = pd.DataFrame(employee_data)
print(employee_df)

#inspectv dataframe
print(employee_df.shape)
print(employee_df.columns)
print(employee_df.dtypes)

#step 5 - head()
print(employee_df.head())

#1st 3 record
print(employee_df.head(3))

#last record
print(employee_df.tail())

#last 2 record
print(employee_df.tail(2))

employee_df.info()
print(employee_df.describe())


print(employee_df["Employee_Name"]);
print(employee_df[
    ["Employee_Name", "Salary"]
    ])
#print(employee_df["Employee_Name", "Salary"])