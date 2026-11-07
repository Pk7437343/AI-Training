use hsbc_bank;

SELECT COUNT(*) AS departments FROM Departments; 

SELECT COUNT(*) AS employees FROM Employees; 

SELECT COUNT(*) AS payroll_rows FROM Payroll; 

SELECT COUNT(*) AS projects FROM Projects; 

SELECT COUNT(*) AS assignments FROM EmployeeProjects; 

SELECT e.employee_id, e.first_name, d.department_name 
FROM Employees e JOIN Departments d ON e.department_id = d.department_id 
ORDER BY e.employee_id LIMIT 10; 


-- Q001. List all databases on the server.
 
show databases;

-- Q002. Select the hsbc_bank database. 
use hsbc_bank;
-- Q003. List all tables in hsbc_bank. 

show tables;

-- Q004. Describe the structure of Employees. 
describe employees;
desc employees;


-- Q005. Describe the structure of Payroll. 

desc payroll;

-- Q006. Display every column of Employees. 
select * from employees;

-- Q007. Display employee_id, first_name and last_name only.
 
 select employee_id, first_name, last_name from employees;


-- Q008. Display distinct designations. 

select distinct designation from employees;

-- Q009. Display distinct department locations. 

select * from departments;
select distinct location from departments;

-- Q010. Retrieve all department names and annual budgets. 
select department_name, annual_budget from departments;

-- Q011. Retrieve the first 10 employees ordered by employee_id. 
select * from employees order by employee_id limit 10;

-- Q012. Create a full_name alias by concatenating first_name and last_name. 

select concat(first_name," ", last_name) as Full_Name from employees;

-- Q013. Show employee name and annualized base salary (base_salary * 12). 
select * from employees;
select first_name, last_name, base_salary*12 as annualized_salary from employees;




select project_name, project_status, budget from projects;
select payroll_id, employee_id, pay_month, basic_pay, bonus, allowances, deductions, net_pay from payroll;
 
-- Level 2 — Filtering, sorting and functions 
select * from employees where base_salary > 90000;
select * from employees where base_salary between 60000 and 110000;
select * from employees where hire_date >= '2024-01-01';
 
select * from employees where employment_status = 'active';
 
select * from employees where first_name LIKE 'A%';
 
select * from employees where last_name like '%a%';
 
select * from employees where  department_id in (1,3,5);
 
select * from employees where manager_id is null;
 
select * from employees order by base_salary desc;
 
select * from employees order by base_salary desc limit 5
 
select*from projects where end_date is null
 
select*from projects where budget> 7000000
 
select * from payroll where payment_status = 'pending';
 
select * from employees where hire_date between '2025-01-01' and '2025-12-31';
 
select upper(concat(first_name,' ',last_name)) as employee_name from employees;
 
select first_name, length(first_name) as name_length from employees;
 
select employee_id ,first_name,year(hire_date) as hire_year from employees;
 
select employee_id,first_name,round(base_salary,-3)as rounded_salary from employees;
 
select * from employees where designation in ('Analyst' , 'Associate');
 
select * from employees where employment_status='Active' order by department_id, base_salary desc;
 
-- Level 3 — Aggregations, GROUP BY and HAVING 
select count(*) from employees;
 
select employment_status,count(employee_id) as emp_count from employees group by employment_status;
 
select min(base_salary) as Min_Salary, max(base_salary) as Max_Salary, avg(base_salary) as Average_Salary from employees;
 
select sum(base_salary) as total_salary from employees;
 
select department_id,count(employee_id) from employees group by department_id;
 
select department_id,avg(base_salary) as Average_Base_Salary from employees group by department_id;
 
select department_id,max(base_salary) as Max_Base_Salary from employees group by department_id;
 
select department_id from employees group by department_id having count(employee_id)>4;
 
select department_id,avg(base_salary) from employees group by department_id having avg(base_salary)>80000;
 


-- Q014. Display all project names, statuses and budgets. 

-- Q015. List payroll records with calculated net_pay. 

-- Level 2 — Filtering, sorting and functions 

-- Q016. Find employees with base_salary greater than 90000. 

-- Q017. Find employees earning between 60000 and 110000. 

-- Q018. Find employees hired on or after 2024-01-01. 

-- Q019. List active employees only. 

-- Q020. Find employees whose first name begins with A. 

-- Q021. Find employees whose last name contains a. 

-- Q022. Find employees in department IDs 1, 3 or 5. 

-- Q023. Find employees with no manager assigned. 

-- Q024. List employees sorted by salary highest first. 

-- Q025. Show the five highest-paid employees. 

-- Q026. List projects with a NULL end_date. 

-- Q027. Find projects with budgets above 7000000. 

-- Q028. Find payroll records whose payment_status is Pending. 

-- Q029. List employees hired during calendar year 2025 using a date range. 

-- Q030. Display employee names in uppercase. 

-- Q031. Show the length of each employee first name. 

-- Q032. Show each employee hire year using YEAR(). 

-- Q033. Display salaries rounded to the nearest thousand. 

-- Q034. Show employees whose designation is Analyst or Associate. 

-- Q035. Show active employees ordered by department and salary descending. 

-- Level 3 — Aggregations, GROUP BY and HAVING 

-- Q036. Count all employees. 

-- Q037. Count active and inactive employees separately. 

-- Q038. Find minimum, maximum and average base salary. 

-- Q039. Calculate the total monthly base salary of all employees. 

-- Q040. Count employees in each department_id. 

-- Q041. Find average base salary by department_id. 

-- Q042. Find highest base salary in each department_id. 

-- Q043. Find departments with more than four employees using HAVING. 

-- Q044. Find departments whose average salary exceeds 80000. 

-- Q045. Count employees by designation. 

-- Q046. Find designations with at least three employees. 

-- Q047. Calculate total net payroll for each pay_month. 

-- Q048. Calculate total bonus paid for each pay_month. 

-- Q049. Find payroll months with total deductions above 200000. 

-- Q050. Count Paid versus Pending payroll rows by month. 

-- Q051. Find the average budget of Active projects. 

-- Q052. Count projects by project_status. 

-- Q053. Find project statuses with more than one project. 

-- Q054. Calculate total project budget by project_type. 

-- Q055. Find departments where the maximum employee salary exceeds 120000. 

-- Level 4 — Two-table joins and reporting 

-- Q056. INNER JOIN Employees and Departments to show employee full name and department name. 

-- Q057. Show employee name, designation and department location using a two-table join. 

-- Q058. List all employees in the Technology department using a join. 

-- Q059. Show employee name, department name and base salary, ordered by salary. 

-- Q060. Count employees per department using Employees JOIN Departments. 

-- Q061. Show department name and average employee salary using JOIN and GROUP BY. 

-- Q062. Find department names with at least five employees using JOIN, GROUP BY and HAVING. 

-- Q063. JOIN Employees and Payroll to show employee name, pay_month and net_pay. 

-- Q064. Find employees whose October 2026 payroll is Pending using two tables. 

-- Q065. Show employee names and bonuses for September 2026. 

-- Q066. Find total net_pay for each employee across three months using Employees and Payroll. 

-- Q067. Show the five employees with the highest total net_pay across all months. 

-- Q068. JOIN EmployeeProjects and Projects to show project names and assignment roles. 

-- Q069. JOIN Employees and EmployeeProjects to list employees and their allocation percentages. 

-- Q070. Count assigned employees per project using Projects and EmployeeProjects. 

-- Q071. Use LEFT JOIN to list every project, including projects with no assignments. 

-- Q072. Use LEFT JOIN to find employees who have no project assignments. 

-- Q073. Use a self JOIN on Employees to show each employee and their manager name. 

-- Q074. Use LEFT self JOIN to include managers who have no manager_id. 

-- Q075. Show employees whose manager earns less than they do using a self JOIN. 

-- Level 5 — Multi-table joins, subqueries and analytics 

-- Q076. Join Employees, Departments and Payroll to show employee, department, month and net pay. 

-- Q077. Find total net payroll by department for October 2026 using three tables. 

-- Q078. Find departments with October 2026 total net payroll greater than 500000. 

-- Q079. Join Employees, EmployeeProjects and Projects to list each employee with project name and role. 

-- Q080. Find all Active projects and the names of employees assigned to them. 

-- Q081. Show the number of distinct projects per employee using a three-table join. 

-- Q082. Find employees assigned to two or more projects using GROUP BY and HAVING. 

-- Q083. Show department names and number of distinct projects worked on by their employees. 

-- Q084. Find the highest-paid employee in each department using a correlated subquery. 

-- Q085. Find employees whose base_salary is above the overall average salary. 

-- Q086. Find employees earning more than their own department average using a correlated subquery. 

-- Q087. Find projects with budgets above the average project budget. 

-- Q088. Find employees who have never received a bonus using NOT EXISTS. 

-- Q089. Find employees who have at least one Pending payroll record using EXISTS. 

-- Q090. Find employees assigned to projects whose budget exceeds 8000000 using IN or EXISTS. 


select designation,count(employee_id) from employees group by designation;
 
select designation from employees group by designation having count(employee_id)>=3;
 
select pay_month,sum(net_pay) from payroll group by pay_month;
 
select pay_month, sum(bonus) from payroll group by pay_month;
 
 
  
select pay_month,payment_status,count(*) from payroll group by pay_month,payment_status;
 
select project_status, avg(budget) from projects group by project_status;
 
select project_status ,count(project_id) from projects group by project_status;
 
select project_status from projects group by project_status having count(project_id)>1;
 
select department_id from employees group by department_id having max(base_salary)>120000;
 



-- Q045. Count employees by designation
SELECT designation, COUNT(*) AS employee_count
FROM Employees
GROUP BY designation;

-- Q046. Find designations with at least three employees
SELECT designation, COUNT(*) AS employee_count
FROM Employees
GROUP BY designation
HAVING COUNT(*) >= 3;

-- Q047. Calculate total net payroll for each pay_month
SELECT pay_month, SUM(net_pay) AS total_net_payroll
FROM Payroll
GROUP BY pay_month;

-- Q048. Calculate total bonus paid for each pay_month
SELECT pay_month, SUM(bonus) AS total_bonus
FROM Payroll
GROUP BY pay_month;

-- Q049. Find payroll months with total deductions above 200000
SELECT pay_month, SUM(deductions) AS total_deductions
FROM Payroll
GROUP BY pay_month
HAVING SUM(deductions) > 200000;

-- Q050. Count Paid versus Pending payroll rows by month
SELECT pay_month, payroll_status, COUNT(*) AS total_count
FROM Payroll
GROUP BY pay_month, payroll_status;

-- Q051. Find the average budget of Active projects
SELECT AVG(budget) AS avg_budget
FROM Projects
WHERE project_status = 'Active';

-- Q052. Count projects by project_status
SELECT project_status, COUNT(*) AS project_count
FROM Projects
GROUP BY project_status;

-- Q053. Find project statuses with more than one project
SELECT project_status, COUNT(*) AS project_count
FROM Projects
GROUP BY project_status
HAVING COUNT(*) > 1;

-- Q054. Calculate total project budget by project_type
SELECT project_type, SUM(budget) AS total_budget
FROM Projects
GROUP BY project_type;

-- Q055. Find departments where the maximum employee salary exceeds 120000
SELECT department_id, MAX(base_salary) AS max_salary
FROM Employees
GROUP BY department_id
HAVING MAX(base_salary) > 120000;

-- Q056. INNER JOIN Employees and Departments to show employee full name and department name
SELECT CONCAT(e.first_name,' ',e.last_name) AS employee_name,
       d.department_name
FROM Employees e
INNER JOIN Departments d
ON e.department_id = d.department_id;

-- Q057. Show employee name, designation and department location
SELECT CONCAT(e.first_name,' ',e.last_name) AS employee_name,
       e.designation,
       d.location
FROM Employees e
JOIN Departments d
ON e.department_id = d.department_id;

-- Q058. List all employees in the Technology department
SELECT CONCAT(e.first_name,' ',e.last_name) AS employee_name
FROM Employees e
JOIN Departments d
ON e.department_id = d.department_id
WHERE d.department_name = 'Technology';

-- Q059. Show employee name, department name and base salary ordered by salary
SELECT CONCAT(e.first_name,' ',e.last_name) AS employee_name,
       d.department_name,
       e.base_salary
FROM Employees e
JOIN Departments d
ON e.department_id = d.department_id
ORDER BY e.base_salary DESC;

-- Q060. Count employees per department
SELECT d.department_name,
       COUNT(e.employee_id) AS employee_count
FROM Departments d
JOIN Employees e
ON d.department_id = e.department_id
GROUP BY d.department_name;

-- Q061. Show department name and average employee salary
SELECT d.department_name,
       AVG(e.base_salary) AS avg_salary
FROM Departments d
JOIN Employees e
ON d.department_id = e.department_id
GROUP BY d.department_name;

-- Q062. Find department names with at least five employees
SELECT d.department_name,
       COUNT(*) AS total_employees
FROM Departments d
JOIN Employees e
ON d.department_id = e.department_id
GROUP BY d.department_name
HAVING COUNT(*) >= 5;

-- Q063. Show employee name, pay_month and net_pay
SELECT CONCAT(e.first_name,' ',e.last_name) AS employee_name,
       p.pay_month,
       p.net_pay
FROM Employees e
JOIN Payroll p
ON e.employee_id = p.employee_id;

-- Q064. Find employees whose October 2026 payroll is Pending
SELECT CONCAT(e.first_name,' ',e.last_name) AS employee_name
FROM Employees e
JOIN Payroll p
ON e.employee_id = p.employee_id
WHERE p.pay_month = '2026-10'
AND p.payroll_status = 'Pending';

-- Q065. Show employee names and bonuses for September 2026
SELECT CONCAT(e.first_name,' ',e.last_name) AS employee_name,
       p.bonus
FROM Employees e
JOIN Payroll p
ON e.employee_id = p.employee_id
WHERE p.pay_month = '2026-09';

-- Q066. Total net_pay for each employee across three months
SELECT CONCAT(e.first_name,' ',e.last_name) AS employee_name,
       SUM(p.net_pay) AS total_net_pay
FROM Employees e
JOIN Payroll p
ON e.employee_id = p.employee_id
GROUP BY e.employee_id,e.first_name,e.last_name;

-- Q067. Five employees with highest total net_pay
SELECT TOP 5
       CONCAT(e.first_name,' ',e.last_name) AS employee_name,
       SUM(p.net_pay) AS total_net_pay
FROM Employees e
JOIN Payroll p
ON e.employee_id = p.employee_id
GROUP BY e.employee_id,e.first_name,e.last_name
ORDER BY total_net_pay DESC;

-- Q068. Project names and assignment roles
SELECT p.project_name,
       ep.assignment_role
FROM EmployeeProjects ep
JOIN Projects p
ON ep.project_id = p.project_id;

-- Q069. Employees and allocation percentages
SELECT CONCAT(e.first_name,' ',e.last_name) AS employee_name,
       ep.allocation_percentage
FROM Employees e
JOIN EmployeeProjects ep
ON e.employee_id = ep.employee_id;

-- Q070. Count assigned employees per project
SELECT p.project_name,
       COUNT(ep.employee_id) AS assigned_employees
FROM Projects p
JOIN EmployeeProjects ep
ON p.project_id = ep.project_id
GROUP BY p.project_name;

-- Q071. List every project, including projects with no assignments
SELECT p.project_name,
       ep.employee_id
FROM Projects p
LEFT JOIN EmployeeProjects ep
ON p.project_id = ep.project_id;

-- Q072. Employees who have no project assignments
SELECT CONCAT(e.first_name,' ',e.last_name) AS employee_name
FROM Employees e
LEFT JOIN EmployeeProjects ep
ON e.employee_id = ep.employee_id
WHERE ep.employee_id IS NULL;

-- Q073. Show each employee and their manager name
SELECT CONCAT(e.first_name,' ',e.last_name) AS employee_name,
       CONCAT(m.first_name,' ',m.last_name) AS manager_name
FROM Employees e
JOIN Employees m
ON e.manager_id = m.employee_id;

-- Q074. Include managers who have no manager_id
SELECT CONCAT(e.first_name,' ',e.last_name) AS employee_name,
       CONCAT(m.first_name,' ',m.last_name) AS manager_name
FROM Employees e
LEFT JOIN Employees m
ON e.manager_id = m.employee_id;

-- Q075. Employees whose manager earns less than they do
SELECT CONCAT(e.first_name,' ',e.last_name) AS employee_name,
       e.base_salary,
       CONCAT(m.first_name,' ',m.last_name) AS manager_name,
       m.base_salary AS manager_salary
FROM Employees e
JOIN Employees m
ON e.manager_id = m.employee_id
WHERE e.base_salary > m.base_salary;

-- Q076. Employee, department, month and net pay
SELECT CONCAT(e.first_name,' ',e.last_name) AS employee_name,
       d.department_name,
       p.pay_month,
       p.net_pay
FROM Employees e
JOIN Departments d
ON e.department_id = d.department_id
JOIN Payroll p
ON e.employee_id = p.employee_id;

-- Q077. Total net payroll by department for October 2026
SELECT d.department_name,
       SUM(p.net_pay) AS total_net_payroll
FROM Departments d
JOIN Employees e
ON d.department_id = e.department_id
JOIN Payroll p
ON e.employee_id = p.employee_id
WHERE p.pay_month = '2026-10'
GROUP BY d.department_name;

-- Q078. Departments with October 2026 payroll greater than 500000
SELECT d.department_name,
       SUM(p.net_pay) AS total_net_payroll
FROM Departments d
JOIN Employees e
ON d.department_id = e.department_id
JOIN Payroll p
ON e.employee_id = p.employee_id
WHERE p.pay_month = '2026-10'
GROUP BY d.department_name
HAVING SUM(p.net_pay) > 500000;

-- Q079. Employee with project name and role
SELECT CONCAT(e.first_name,' ',e.last_name) AS employee_name,
       p.project_name,
       ep.assignment_role
FROM Employees e
JOIN EmployeeProjects ep
ON e.employee_id = ep.employee_id
JOIN Projects p
ON ep.project_id = p.project_id;

-- Q080. Active projects and assigned employees
SELECT p.project_name,
       CONCAT(e.first_name,' ',e.last_name) AS employee_name
FROM Projects p
JOIN EmployeeProjects ep
ON p.project_id = ep.project_id
JOIN Employees e
ON ep.employee_id = e.employee_id
WHERE p.project_status = 'Active';

-- Q081. Number of distinct projects per employee
SELECT CONCAT(e.first_name,' ',e.last_name) AS employee_name,
       COUNT(DISTINCT ep.project_id) AS project_count
FROM Employees e
JOIN EmployeeProjects ep
ON e.employee_id = ep.employee_id
JOIN Projects p
ON ep.project_id = p.project_id
GROUP BY e.employee_id,e.first_name,e.last_name;

-- Q082. Employees assigned to two or more projects
SELECT CONCAT(e.first_name,' ',e.last_name) AS employee_name,
       COUNT(DISTINCT ep.project_id) AS project_count
FROM Employees e
JOIN EmployeeProjects ep
ON e.employee_id = ep.employee_id
GROUP BY e.employee_id,e.first_name,e.last_name
HAVING COUNT(DISTINCT ep.project_id) >= 2;

-- Q083. Department names and number of distinct projects
SELECT d.department_name,
       COUNT(DISTINCT ep.project_id) AS project_count
FROM Departments d
JOIN Employees e
ON d.department_id = e.department_id
JOIN EmployeeProjects ep
ON e.employee_id = ep.employee_id
GROUP BY d.department_name;

-- Q084. Highest-paid employee in each department
SELECT *
FROM Employees e
WHERE e.base_salary =
(
    SELECT MAX(e2.base_salary)
    FROM Employees e2
    WHERE e2.department_id = e.department_id
);

-- Q085. Employees whose salary is above overall average
SELECT *
FROM Employees
WHERE base_salary >
(
    SELECT AVG(base_salary)
    FROM Employees
);

-- Q086. Employees earning more than department average
SELECT *
FROM Employees e
WHERE e.base_salary >
(
    SELECT AVG(e2.base_salary)
    FROM Employees e2
    WHERE e2.department_id = e.department_id
);

-- Q087. Projects with budgets above average budget
SELECT *
FROM Projects
WHERE budget >
(
    SELECT AVG(budget)
    FROM Projects
);

-- Q088. Employees who have never received a bonus
SELECT *
FROM Employees e
WHERE NOT EXISTS
(
    SELECT 1
    FROM Payroll p
    WHERE p.employee_id = e.employee_id
    AND p.bonus > 0
);

-- Q089. Employees who have at least one Pending payroll record
SELECT *
FROM Employees e
WHERE EXISTS
(
    SELECT 1
    FROM Payroll p
    WHERE p.employee_id = e.employee_id
    AND p.payroll_status = 'Pending'
);

-- Q090. Employees assigned to projects with budget above 8000000
SELECT *
FROM Employees e
WHERE EXISTS
(
    SELECT 1
    FROM EmployeeProjects ep
    JOIN Projects p
    ON ep.project_id = p.project_id
    WHERE ep.employee_id = e.employee_id
    AND p.budget > 8000000
);











-- Q091. Use CASE to classify salaries as High (>= 100000), Medium (>= 70000) or Low. 

-- Q092. Use CASE to categorize project budgets as Large (>= 8000000) or Standard. 

-- Q093. Use a CTE to calculate total net_pay per employee and return the top ten. 

-- Q094. Use a CTE to calculate departmental average salary and return above-average departments. 

-- Q095. Build a final dashboard query showing each department, employee count, average base salary, and October 2026 total net payroll; include departments with no employees. 

-- Q096. Find the project with the greatest number of assigned employees. 

-- Q097. Find employees whose total project allocation exceeds 100 percent. 

-- Q098. Compare each employee October net pay against the department October average using a CTE. 

-- Q099. Find departments with no employees assigned to any Active project using NOT EXISTS. 

-- Q100. Rank employees by base salary within each department using DENSE_RANK(). 

 
