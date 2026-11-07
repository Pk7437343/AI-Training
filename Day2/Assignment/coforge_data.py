import pandas as pd
import numpy as np
 
employees = pd.read_excel("coforge_employees_50.xlsx")
projects = pd.read_csv("coforge_projects.csv")
 
print(employees.head())
print(projects.head())
merged = employees.merge(projects, on="ProjectID", how="left")
 
 
#1#
# 1. Load the employee CSV into a DataFrame.
print(employees)
 
#2#
# 2. Display the first five and last five rows.
print(employees.head())
print(employees.tail())
 
#3#
# 3. Show shape, column names and data types.
print(employees.shape)
print(employees.columns)
print(employees.dtypes)
 
#4#
# 4. Run info() and describe() and explain the results.
employees.info()
print(employees.describe())
 
#5#
# 5. Select EmployeeName, Department, Salary and PerformanceRating.
print(employees[["EmployeeName", "Department", "Salary", "PerformanceRating"]])
 
#6#
# 6. Calculate minimum, maximum and mean salary.
print("Min Salary :", employees["Salary"].min())
print("Max Salary :", employees["Salary"].max())
print("Mean Salary :", employees["Salary"].mean())
 
#7#
# 7. Calculate total annual salary expenditure.
print("Total Salary :", employees["Salary"].sum())
 
#8#
# 8. Identify the youngest and oldest employees.
youngest = employees[employees["Age"] == employees["Age"].min()]
print("Youngest Employee")
print(youngest)
 
oldest = employees[employees["Age"] == employees["Age"].max()]
print("Oldest Employee")
print(oldest)
 
#9#
# 9. Count employees in each department.
print(employees["Department"].value_counts())
 
#10#
# 10. Count employees in each office location.
print(employees["Location"].value_counts())
 
#11#
# 11. List unique designations and their counts.
print(employees["Designation"].value_counts())
 
#12#
# 12. Filter employees with Salary above INR 1,000,000.
print(employees[employees["Salary"] > 1000000])
 
#13#
# 13. Filter employees with PerformanceRating >= 4.
print(employees[employees["PerformanceRating"] >= 4])
 
#14#
# 14. Sort by Salary from highest to lowest.
print(employees.sort_values("Salary", ascending=False))
 
#15#
# 15. Display the five highest-paid employees.
print(employees.sort_values("Salary", ascending=False).head(5))
 
#16#
# 16. Find mean salary by department using groupby().
print(employees.groupby("Department")["Salary"].mean())
 
#17#
# 17. Find minimum and maximum salary by designation.
print("Minimum Salary by designation : ")
print(employees.groupby("Designation")["Salary"].min())
print("Maximum Salary by designation : ")
print(employees.groupby("Designation")["Salary"].max())
 
#18#
# 18. Find mean performance rating by location.
print(employees.groupby("Location")["PerformanceRating"].mean())
 
#19#
# 19. Count employees grouped by Department and Gender.
print(employees.groupby(["Department","Gender"]).size())
 
#20#
# 20. Filter employees with ExperienceYears > 5 and PerformanceRating >= 4.
print(employees[(employees["ExperienceYears"] > 5) & (employees["PerformanceRating"] >= 4)])
 
#21#
# 21. Use isin() to filter employees from any three selected locations.
print(employees[employees["Location"].isin(["Pune","Mumbai","Bangalore"])])
 
#22#
# 22. Create SalaryCategory (Low, Medium, High); document your thresholds.
employees["SalaryCategory"] = np.where(employees["Salary"] < 30000,"Low",np.where(employees["Salary"] <= 60000, "Medium", "High"))
print(employees[["Salary", "SalaryCategory"]])
 
#23#
# 23. Create PerformanceCategory using clear rating thresholds.
employees["PerformanceCategory"] = np.where(
    employees["PerformanceRating"] < 3,
    "Poor",
    np.where(employees["PerformanceRating"] <= 4, "Average", "Excellent")
)
 
print(employees[["PerformanceRating", "PerformanceCategory"]])
 
#24#
# 24. Calculate salary per year of experience; handle zero experience safely.
employees["SalaryPerYear"] = np.where(
    employees["ExperienceYears"] == 0,
    0,
    employees["Salary"] / employees["ExperienceYears"]
)
print(employees[["Salary","SalaryPerYear"]])
 
#25#
# 25. Calculate total Salary and Bonus by department.
print(employees.groupby("Department")[["Salary", "Bonus"]].sum())
 
#26#
# 26. Calculate average TrainingHours by department.
print(employees.groupby("Department")["TrainingHours"].mean())
 
#27#
# 27. Identify employees with LeaveDays > 15.
print(employees[employees["LeaveDays"] > 15])
 
#28#
# 28. Calculate correlation between Salary and ExperienceYears.
print(employees["Salary"].corr(employees["ExperienceYears"]))
 
#29#
# 29. Calculate correlation between TrainingHours and PerformanceRating.
print(employees["TrainingHours"].corr(employees["PerformanceRating"]))
 
#30#
# 30. Group by Department and Designation; show headcount and mean salary.
grouped = employees.groupby(["Department", "Designation"])
print(grouped["Salary"].mean())
print(grouped["EmployeeID"].count())
 
#31#
# 31. Use agg() to find count, min, max, mean and median salary by department.
print(employees.groupby("Department")["Salary"]
      .agg(["count","min","max","mean","median"]
))
 
 
 
#35#
# 35. Inspect nulls and duplicates; report findings and clean only where justified.
print("Null Values : ")
print(employees.isnull().sum())
 
print("Duplicated Values : ")
print(employees.duplicated().sum())
 
#36#
# 36. Merge employees with projects using ProjectID.
merged = employees.merge(projects, on="ProjectID", how="left")
print(merged)
 
#37#
# 37. Compare inner, left, right and outer joins; explain row-count differences.
inner_join = employees.merge(projects, on="ProjectID", how="inner")
left_join = employees.merge(projects, on="ProjectID", how="left")
right_join = employees.merge(projects, on="ProjectID", how="right")
outer_join = employees.merge(projects, on="ProjectID", how="outer")
 
print("Inner Join Rows :", len(inner_join))
print("Left Join Rows  :", len(left_join))
print("Right Join Rows :", len(right_join))
print("Outer Join Rows :", len(outer_join))
 
#38#
# 38. Find employees on projects with ProjectBudgetINR > 10,000,000.
print(merged[merged["ProjectBudgetINR"] > 10000000])
 
#39#
# 39. Rank employees by Salary within each department.
employees["SalaryRank"] = employees.groupby("Department")["Salary"].rank(ascending=False)
print(employees[["EmployeeName", "Department","Salary", "SalaryRank"]])
 
#40#
# 40. Find the top three highest-paid employees per department.
print(
    employees.sort_values("Salary",ascending=False)
    .groupby("Department")
    .head(3)
)
 
#41#
# 41. Use transform() to compute Salary minus department mean Salary.
employees["SalaryDiff"] = (employees["Salary"]- employees.groupby("Department")["Salary"].transform("mean"))
print(employees["SalaryDiff"])
 
 
 
#44#
# 44. Create a weighted performance score from PerformanceRating, TrainingHours and ProjectsCompleted.
employees["PerformanceScore"] = (employees["PerformanceRating"] * 0.5+ employees["TrainingHours"] * 0.2+ employees["ProjectsCompleted"] * 0.3)
print(employees[["EmployeeName", "PerformanceScore"]])
 
#45#
# 45. Create and query a MultiIndex by Department and Location.
multi_df = employees.set_index(["Department", "Location"])
print(multi_df)
 
 
#47#
# 47. Calculate cumulative Salary by department after sorting by Salary.
print(employees.sort_values(["Department","Salary"]).groupby("Department")["Salary"].cumsum())
 
