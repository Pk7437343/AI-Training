show databases
use hsbc_bank
show tables
desc employees
desc payroll
select *from employees
select employee_id, first_name , last_name from employees
select distinct designation from employees
select distinct location from departments
select department_name, annual_budget from departments
select * from employees order by employee_id limit 10
select concat(first_name,'',last_name) as full_name from employees
select concat(first_name,' ',last_name) as employee_name, base_salary * 12 as annual_salary  from employees
select project_name, project_status, budget from projects
select payroll_id, employee_id, pay_month, basic_pay, bonus, allowances, deductions, net_pay from payroll
 
-- Level 2 — Filtering, sorting and functions 
select * from employees where base_salary > 90000;
select * from employees where base_salary between 60000 and 110000;
select * from employees where hire_date >= '2024-01-01'
 
select * from employees where employment_status = 'active'
 
select * from employees where first_name LIKE 'A%'
 
select * from employees where last_name like '%a%'
 
select * from employees where  department_id in (1,3,5)
 
select * from employees where manager_id is null
 
select * from employees order by base_salary desc
 
select * from employees order by base_salary desc limit 5
 
select*from projects where end_date is null
 
select*from projects where budget> 7000000
 
select * from payroll where payment_status = 'pending'
 
select * from employees where hire_date between '2025-01-01' and '2025-12-31';
 
select upper(concat(first_name,' ',last_name)) as employee_name from employees
 
select first_name, length(first_name) as name_length from employees
 
select employee_id ,first_name,year(hire_date) as hire_year from employees
 
select employee_id,first_name,round(base_salary,-3)as rounded_salary from employees
 
select * from employees where designation in ('Analyst' , 'Associate')
 
select * from employees where employment_status='Active' order by department_id, base_salary desc;
 
-- Level 3 — Aggregations, GROUP BY and HAVING 
select count(*) from employees
 
select employment_status,count(employee_id) as emp_count from employees group by employment_status
 
select min(base_salary) as Min_Salary, max(base_salary) as Max_Salary, avg(base_salary) as Average_Salary from employees
 
select sum(base_salary) as total_salary from employees
 
select department_id,count(employee_id) from employees group by department_id
 
select department_id,avg(base_salary) as Average_Base_Salary from employees group by department_id
 
select department_id,max(base_salary) as Max_Base_Salary from employees group by department_id
 
select department_id from employees group by department_id having count(employee_id)>4
 
select department_id,avg(base_salary) from employees group by department_id having avg(base_salary)>80000
 
select designation,count(employee_id) from employees group by designation
 
select designation from employees group by designation having count(employee_id)>=3
 
select pay_month,sum(net_pay) from payroll group by pay_month
 
select pay_month, sum(bonus) from payroll group by pay_month
 
select pay_month,payment_status,count(*) from payroll group by pay_month,payment_status
 
select project_status ,avg(budget) from projects group by project_status
 
select project_status ,count(project_id) from projects group by project_status
 
select project_status from projects group by project_status having count(project_id)>1
 
select department_id from employees group by department_id having max(base_salary)>120000
 