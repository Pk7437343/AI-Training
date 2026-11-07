AI-Training

Training → Classwork and examples
Assignments → Practice exercises and solutions
Day 1 – Python Basics
Training
Taking user input and type conversion
Area, perimeter, temperature and distance conversion programs
Average marks calculator
if, elif, else statements
Salary bonus, discount calculator, BMI calculator
for loops, range(), break, and continue
Lists and list slicing
Assignments
Employee bonus calculator
Loan approval system
Income tax calculator
Insurance premium calculator
Number filtering using loops
Amount validation using while
Vowel and consonant counter
Log monitoring programs
Day 2 – NumPy & Pandas
Training
Pandas Series and DataFrames
head(), tail(), describe()
Column selection and row filtering
Creating new columns
Sorting datasets
Aggregate functions (min, max, sum, mean)
Top-N records
NumPy arrays, indexing, slicing
Shape, size and standard deviation
Dataset merging and joins
Assignments / Datasets
HSBC_Synthetic_Banking_Customers.csv
coforge_employees_50.xlsx
coforge_projects.csv
Day 3 – MySQL
Training
Creating databases and tables
Inserting records
SELECT, WHERE, BETWEEN
IN, LIKE
ORDER BY
LIMIT
Aggregate Functions:
COUNT()
MIN()
MAX()
AVG()
SUM()
GROUP BY
HAVING
Assignments
HSBC HR & Payroll Database

Contains:

Assignment document
SQL solutions
Output screenshots/files
Day 4 – FastAPI
Training
REST API development using FastAPI
SQLAlchemy ORM
Pydantic validation
MySQL integration
Environment configuration using .env
Logging implementation
CRUD Operations:
GET
POST
PUT
DELETE
Project Structure
project/
│
├── config/
├── models/
├── schemas/
├── services/
├── main.py
└── .env

Projects
CoforgeCustomerDB
TrainingFeedback
Assignments
SQL Setup
Database creation scripts
Table creation scripts
API Case Studies
Employee Performance Management
Cricket Player Management
Training Feedback System
Inventory Product Management
Banking Customer Management

Each project includes:

Create Record
List Records (Pagination)
Get By ID
Update Record
Delete Record
FastAPI Setup Commands
Step 1: Create Virtual Environment
python -m venv venv
venv\Scripts\activate

Step 2: Install Required Packages
pip install fastapi uvicorn python-dotenv pydantic sqlalchemy pymysql pydantic-settings email-validator

Step 3: Generate Requirements File
pip freeze > requirements.txt

Step 4: Create Project Files
type nul > database.py
type nul > customer_models.py
type nul > customer_schemas.py
type nul > customer_services.py
type nul > main.py

Step 5: Run Application
uvicorn main:app --reload


Open:

http://127.0.0.1:8000/docs

Day 5 – ETL Pipeline
Project: ecommerce_etl_pipeline
Extract

Read data from:

customers.csv
orders.csv
payments.csv
deliveries.csv
Transform
Remove duplicate records
Handle missing values
Standardize date formats
Clean text fields
Calculate total order amount
Join

Merge all datasets into a single consolidated dataset.

Report

Generate:

Total Orders
Total Revenue
Business Summary Report
Technologies Used
Python
NumPy
Pandas
MySQL
SQLAlchemy
FastAPI
Pydantic
REST APIs
ETL Processing
Git & GitHub
Author

Prince Kumar
 GitHub: https://github.com/Pk7437343

This repository contains all training materials, assignments, solutions, datasets, and projects completed during the AI Training Program.
