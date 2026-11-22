import pandas as pd
finance = pd.read_csv("data/employees/finance_employees.csv")
hr= pd.read_csv("data/employees/hr_employees.csv")
it=pd.read_csv("data/employees/it_employees.csv")
operation=pd.read_csv("data/employees/operations_employees.csv")
sale= pd.read_csv("data/employees/sales_employees.csv")

employee_df = pd.concat([finance, hr, it, operation, sale])
print(employee_df)

print(employee_df.head(20))

print(employee_df.tail(20))
print("======")
department_wise_sum = employee_df.groupby("department")["emp_id"].count()
print(department_wise_sum)

print(employee_df.columns) #and dtype

print(employee_df[employee_df.isna()])

print([employee_df.duplicated(subset="emp_id")])

print(employee_df.groupby("department")["emp_id"])

city_count = employee_df["city"].nunique()
print(city_count)



# #section 2

work_in_it = employee_df[employee_df["department"]=="IT"].count()
print(work_in_it)

print(employee_df[employee_df["department"]=="Finance"])

print("==")

print(employee_df[ (employee_df["department"]=="Finance") & (employee_df["salary"]>80000)])

print(employee_df[employee_df["salary"]>100000])

print(employee_df[(employee_df["salary"]>50000) & (employee_df["salary"]<80000)])

finder = employee_df[(employee_df["department"]=="IT") & (employee_df["city"]=="Bangalore")]
print(finder)

which_depart = employee_df[(employee_df["department"]=="HR") | (employee_df["department"]=="Sales")]
print(which_depart)

less = employee_df[(employee_df["salary"]<40000) & (employee_df["city"]=="Delhi")]
print(less)



total_salary = employee_df.groupby("department")["salary"].sum()
print(total_salary)


print("find")
find = employee_df[employee_df["city"]!="Mumbai"]
print(find)

total_salary_it = employee_df[employee_df["department"]=="IT"].sum()
print(f"total {total_salary_it}")



g = employee_df[employee_df["department"] == "IT"].groupby("department")["salary", "city"]
print(g)

it_employees = employee_df[employee_df["department"] == "IT"][["city", "salary"]]

print(it_employees)


tot_hr = employee_df[employee_df["department"]=="HR"]["salary"].sum()
print(tot_hr)

tot_hr = employee_df[employee_df["department"] == "HR"]["salary"].sum()

print(tot_hr)


tot_sales = employee_df[employee_df["department"]=="Sales"]["salary"].sum()
print(tot_sales)

print(employee_df.groupby("department")["salary"].sum())

print(employee_df.groupby("city")["salary"].sum())


two_combined = employee_df["department"].isin(["IT","Finance"]).sum()
print(two_combined)

total_salary_by_dept = employee_df.groupby("department")["salary"].sum()
print(total_salary_by_dept)
all_contri = total_salary_by_dept.sum()
print(all_contri)

percentage = (total_salary_by_dept/all_contri)*100
print(percentage)

percentage = (
    employee_df.groupby("department")["salary"].sum()/employee_df["salary"].sum()) * 100

print(percentage.sort_values(ascending=False))

find_max_salary = employee_df["salary"].max()
print(find_max_salary)

find_min = employee_df["salary"].min()
print(find_min)

dept_wise = employee_df.groupby("department")["salary"].min()
print(dept_wise)

dept_wise = employee_df.groupby("department")["salary"].max()
print(dept_wise)

dept_wise = employee_df.groupby("department")["salary"].mean()
print(dept_wise)

salary_pune= employee_df[employee_df["city"]=="pune"]["salary"].mean() 
print(salary_pune)

finder_sal_dif = employee_df.groupby("department")["salary"].max()-employee_df.groupby("department")["salary"].mean()
print(finder_sal_dif)

grp = employee_df.groupby("department")["emp_id"].count()
print(grp)
grp_city = employee_df.groupby("city")["emp_id"].count()
print(grp_city)
print("===========section===5")
grp_agg = employee_df.groupby("department")["salary"].agg(["sum", "min", "max", "mean"])
print(grp_agg)

grp_agg = employee_df.groupby("department").agg({
    "salary": ["sum", "mean", "min", "max"]
})

print(grp_agg)


db_grp = employee_df.groupby(["department","city"])["salary"].sum()
print(db_grp)

finnd = employee_df.groupby("department")["salary"].sum().sort_values().tail(1)
print(finnd)

finnder = employee_df.groupby("department")["salary"].sum().sort_values().head(1)
print(finnder)

finnd = employee_df.groupby("department")["salary"].mean().sort_values().tail(1)
print(finnd)

finnd = employee_df.groupby("department")["salary"].mean().sort_values().head(1)
print(finnd)

finddery = employee_df.groupby("city")["emp_id"].count()
print(finddery)

ddd = employee_df.groupby("department")["salary"].sum().sort_values(ascending=False)
print(ddd)




ff = employee_df.groupby("department")["salary"].sum()
tt = ff[ff>1000000]
print(ff)

ff = employee_df.groupby("city")["salary"].sum()
tt = ff[ff>15000000]
print(ff)

ddd= employee_df.groupby("department")["city"].agg({
    "salary":"sum"
})
print(ddd)