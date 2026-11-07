use Coforge_db;

select * from Employee where EmpSalary>50000;

select * from Employee where EmpAge<25;

select * from Employee where EmpSalary=45000;

select * from Employee where EmpCity<>'pune';

select * from Employee where EmpSalary between 40000 AND 45000;

select * from Employee where EmpCity in('pune','delhi');

select * from Employee where EmpAge between 25 And 27;

select * from Employee where EmpCity='pune' And EmpSalary>45000;

select * from Employee where EmpName Like '%sh%';

select * from Employee order by Empsalary DESC;


select * from Employee order by EmpSalary DESC LIMIT 5;

select * from Employee order by EmpCity, EmpSalary DESC;

select COUNT(*) as 'Total Employee' from Employee;

select MIN(EmpSalary) as 'Minimum Salary' from Employee;


select MAX(EmpSalary) as 'Maximum Salary' from Employee;

select ROUND(AVG(Empsalary),2) as 'Average Salary' from Employee;

select SUM(EmpSalary) as 'Employee Expenditure' from Employee;

select COUNT(EmpSalary) as 'Greater than 50k' from Employee where EmpSalary>50000;

select MAX(EmpSalary)-MIN(EmpSalary) from Employee;

select EmpCity, COUNT(EmpCity) as 'count city' from Employee group by EmpCity, EmpName;

-- calculate each city -salary, min, and max, and total expenditure in each city;


select EmpCity, MIN(EmpSalary), Max(EmpSalary), SUM(EmpSalary) as 'Total Expenditure', COUNT(EmpCity) as 'count city' from Employee group by EmpCity, EmpName;

select EmpCity, COUNT(EmpID) as 'Employee Count' from Employee group by EmpCity having Count(EmpCity)>4;

select EmpCity, AVG(EmpSalary) as 'Average Salary' from Employee group by EmpCity having AVG(EmpSalary)>50000;

select EmpAge, COUNT(EmpID) as 'Total Employee' from Employee group by EmpAge having COUNT(EmpAge)>3;

