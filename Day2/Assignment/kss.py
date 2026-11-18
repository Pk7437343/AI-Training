import pandas as pd
employee = pd.DataFrame({
    "empid":[1,2,3],
    "empname":["aman", "prince", "ramesh"]
    "emp_age":[23,32,34],
    "dept_id":[101,102,103]
})
department = pd.DataFrame({
    "dept_id":[1,2,3],
    "dept_name":["IT", "CC", "DD"]
})

merged_df = pd.merge(employee, department, on="dept_id", how="inner")

result= merged_df.groupby("employee")["department"].agg([
    "min", "sum"
])
print(result)