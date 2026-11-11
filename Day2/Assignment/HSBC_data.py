import pandas as pd
import numpy as np
df = pd.read_csv("HSBC_Synthetic_Banking_Customers.csv")


#1. Convert Account_Balance into a NumPy array.
monthly_deposit = np.array(df.Monthly_Deposit)
monthly_withdrawl = np.array(df.Monthly_Withdrawal) 
Branch_wise = np.array(df["Branch"])
salary = np.array(df["Account_Balance"])
print(type(salary))

#2. Inspect array ndim, shape, size and dtype. 
print("array : ", salary)
print("Dimension : ", salary.ndim)
print("shape : ", salary.shape)
print("size  : ", salary.size)
print("dtype  :", salary.dtype)

#3. Calculate minimum and maximum balances. 
minimum_balance = salary.min()
print(minimum_balance)

maximum_balance = salary.max()
print(maximum_balance)

#Calculate sum, mean, median and standard deviation of balances. 
print("sum of balances", salary.sum())
print("mean of balance : ", salary.mean())
print("mean of balance : ", np.mean(salary))
print("median balance", np.median(salary))
print("standard deviation", np.std(salary))

# Find the 25th, 50th and 75th balance percentiles. 
percentile = np.percentile(df['Account_Balance'], [25, 50, 75])
 
print(percentile)

# Filter balances above INR 500,000. 
print("Salary above 500000", salary[salary>50000])


# Identify credit scores below 650 using boolean masking. 
credit = np.array(df.Credit_Score)
print("Credit_score", credit<650)    

# Sort balances ascending and descending. 
ascending = np.sort(salary)
 
descending = np.sort(salary)[::-1]
 
print(ascending)
print(descending)

#print("sorted salary", salary.sort())

print("sorted salary", df["Account_Balance"].sort_values(ascending=False)) #pandas

# Compute total monthly deposits and total monthly withdrawals. 

print("total monthly deposits :" , monthly_deposit.sum())
print("total monthly withdrawal", monthly_withdrawl.sum())


# Use vectorization to calculate hypothetical balances after a 5% increase. 
print("hypothetical balance", salary*1.05)

#10. Use vectorization to calculate hypothetical balances after a 5% increase. 

#11. Use np.where to classify balances as High (> INR 500,000) or Low. 

classify = np.where(salary>500000, "High", "low")
print(classify)

# 12. Use np.select to categorize balances into Low (< INR 100,000), Medium (INR 100,000–500,000) and High (> INR 500,000). 

# categorize = np.select([
#     (salary<100000), 
#     ((salary>=100000) & (salary<=500000)),
#     (salary>500000)
#     ],
#     ["low", "Medium", "High"]
# )
# print(categorize)





# conditions = np.array[
#     salary < 100000,
#     (salary >= 100000) & (salary <= 500000),
#     salary > 500000
# ]

# labels = ["Low", "Medium", "High"]

# result = np.select(conditions, labels)

# print(result)







# 13. Compute deposit-to-income ratio; handle zero income safely. 

ratio = np.divide(
    df['Monthly_Deposit'],
    df['Monthly_Income'],
    out=np.zeros(len(df)),
    where=df['Monthly_Income'] != 0
)
 
print(ratio)


# 14. Identify records where monthly withdrawals exceed monthly deposits. 

exceed = np.where(monthly_withdrawl>monthly_deposit)
print("exceed monthly withdrawals exceed monthly deposits. ", exceed)

print("exceed withdrawls :", monthly_deposit[monthly_withdrawl>monthly_deposit])

# 15. Use np.unique to summarize credit-score frequencies. 

summarize_credit = np.unique(df["Credit_Score"])
print("summarize credit score ", summarize_credit)

summarize_credit = np.unique(df["Credit_Score"])
print("summarize credit score ", len(summarize_credit))
# 16. Use np.argsort to locate the five largest balances. 

five_largest = np.argsort(salary) #return index
print("the five largest : ", salary[five_largest[-5:]])

# 17. Perform min-max normalization of balances; handle constant arrays safely. 


mean = np.mean(salary)
std = np.std(salary)
 
if std != 0:
    z_score = (salary - mean) / std
else:
    z_score = np.zeros(len(salary))
 
print(z_score)
# 18. Compute z-scores for balances; handle zero standard deviation safely.

mean = np.mean(salary)
std = np.std(salary)

if std != 0:
    z_score = (salary - mean) / std
else:
    z_score = np.zeros(len(salary))

print(z_score) 


#19
data = np.column_stack((
    salary,
    df['Monthly_Deposit'],
    df['Monthly_Withdrawal']
))
 
print(data)
 
print(np.sum(data, axis=0))
print(np.sum(data, axis=1))





# 19. Build a 2D array with balance, deposit and withdrawal columns and inspect axis-wise totals. 

build_array = [[salary, monthly_deposit, monthly_withdrawl]]
print("print array", build_array)



# 20. Calculate Pearson correlation between income and account balance. 
correlation = np.corrcoef(
    df['Monthly_Income'],
    df['Account_Balance']
)
 
print(correlation)



# Read the supplied CSV using pd.read_csv. 

df = pd.read_csv("HSBC_Synthetic_Banking_Customers.csv")

# 22. Display first and last ten rows. 
print(df.head(10))
print(df.tail(10))


print(df.info)
# 23. Inspect shape, columns, dtypes and info(). 
print("database shape", df.shape)
print("database size", df.size)
print("colums", df.columns)
print("dtype", df.dtypes)



# 24. Generate numerical descriptive statistics using describe(). 
print("describe" , df.describe())

# 25. Check missing values and duplicate Customer_ID values. 

print("duplicate ",df.duplicated().sum())
print("null check", df.isnull().sum())

# 26. Select customer name, city, balance and credit score columns. 
result = df[["Customer_Name", "City", "Account_Balance", "Credit_Score"]]
print(result)

# 27. Filter customers aged 25 through 40 inclusive. 
result_age = df[(df["Age"]>=25) & (df["Age"]<=40)]
print("Age", result_age)

# 28. Find active Savings accounts. 
active_acc =df[
    (df["Account_Status"]=="Active") & 
    (df["Account_Type"]=="Savings")]
print("account status", active_acc)
 # 29. Sort by balance and monthly income, descending. 

sort_bal_income = df.sort_values(
    by=["Account_Balance", "Monthly_Income"], ascending=False)
print(sort_bal_income)

# 30. Create Net_Monthly_Flow = Monthly_Deposit - Monthly_Withdrawal. 

Net_Monthly_Flow = df["Monthly_Deposit"].sum()-df["Monthly_Withdrawal"].sum()
print(Net_Monthly_Flow)


# 31. Group by City and calculate total Account_Balance. 


df[Net_Monthly_Flow] = df["Monthly_Deposit"]-df["Monthly_Withdrawal"]
print(Net_Monthly_Flow)



# 32. Group by Account_Type and calculate average Monthly_Income. 

# print(df[[
#     "Customer_Name",
#     "Account_Type",
#     "Monthly_Income"
# ]])

res = df.groupby("Account_Type")["Monthly_Income"].mean()
print(res)


# 33. Compute branch-wise deposit and withdrawal totals. 
print("Branch wise total")

Branch_wise_total = df.groupby("Branch").agg({
    "Monthly_Deposit": "sum",
    "Monthly_Withdrawal": "sum"
    })

print(Branch_wise_total)


# 34. Use agg to report minimum, maximum, mean and median balances by branch.
Branch_wise_report = df.groupby("Branch").agg({
    "Account_Balance": "min",
    "Account_Balance": "max",
    "Account_Balance": "mean",
    "Account_Balance": "median",

 })
print(Branch_wise_report)

print("again")
Branch_wise_report1 = df.groupby("Branch")["Account_Balance"].agg({
    "min", "max", "mean", "median"

 })
print(Branch_wise_report1)

# 35. Create a pivot table of total balance by City and Account_Type. 
pivot = pd.pivot_table(df,
    index = "City",
    columns="Account_Type",
    values="Account_Balance",
    aggfunc="sum",
    
)
print(pivot)

# 36. Use pd.cut to create age groups: 18–25, 26–40, 41–60 and 61+. 
bins = [17, 25, 40,60, float('inf')]
labels = ['18-25', '26-40', '41-60', '61+']

df["Age_Group"] = pd.cut(
    df["Age"], 
    bins = bins,
    labels= labels
)
print(df[['Customer_Name', 'Age', 'Age_Group']])

# 37. Use groupby().transform() to calculate each customer’s balance minus branch average. 
df["Branch_Average"] = df.groupby("Branch")["Account_Balance"].transform("mean")
df["Balance_Difference"] =(
    df["Account_Balance"] - df["Branch_Average"]
)
print(df[["Customer_Name", "Branch", "Account_Balance", "Branch_Average", "Balance_Difference"]])

# 38. Create a separate Branch_Details DataFrame with Branch and Region; merge it on Branch and validate the join. 

Branch_Details = pd.DataFrame({
    'Branch': ['Branch_A', 'Branch_B', 'Branch_C'],
    'Region': ['North', 'South', 'East']
})
 
df = df.merge(
    Branch_Details,
    on='Branch',
    how='left',
    validate='many_to_one',
    indicator=True
)
 
print(df[['Branch', 'Region', '_merge']])

# 39. Find the top three customers by balance within each City. 

top_customers = (
    df.sort_values('Account_Balance', ascending=False)
      .groupby('City')
      .head(3)
)
 
print(top_customers[['Customer_Name', 'City', 'Account_Balance']])

# 40. Create a branch summary with total balance, mean credit score, counts by account status and total net monthly flow
df["Net_Monthly_Flow"] = df["Monthly_Deposit"]-df["Monthly_Withdrawal"]
branch_summary = df.groupby('Branch').agg(
    Total_Balance=('Account_Balance', 'sum'),
    Mean_Credit_Score=('Credit_Score', 'mean'),
    Total_Net_Monthly_Flow=('Net_Monthly_Flow', 'sum')
)
 
status_counts = pd.crosstab(
    df['Branch'],
    df['Account_Status']
)
 
branch_summary = branch_summary.join(status_counts)
 
print(branch_summary)