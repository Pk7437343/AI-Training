from langchain.tools import tool

@tool
def calculate_basic_salary(basic_salary: float)->dict:
    """Validate and return the employee basic salary"""
    if basic_salary<0:
        raise ValueError("basic salary is negative")
    return {
        "basic_salary": round(basic_salary,2)
    }

@tool
def calculate_hra(basic_salary: float, hra_percentage: float)->dict:
    """Calculate HRA amount."""
    if basic_salary<0:
        raise ValueError("Basic Salary cant negative")
    if not 0<= hra_percentage<=100:
        raise ValueError("Invalid da percentage")
    hra = basic_salary*hra_percentage/100
    return {
       "hra": round(hra,2)
    }    


@tool
def calculate_da(basic_salary: float, da_percentage:float)->dict:
    """Calculate DA amount."""
    if basic_salary<0:
        raise ValueError("Basic Salary cant negative")
    if not 0 <= da_percentage<=100:
        raise ValueError("Invalid da percentage")
    da = basic_salary*da_percentage/100
    
    return {
       "da": round(da,2)
    }

@tool
def calculate_gross_salary(basic_salary:float, hra:float, da:float)->dict:
    """Calculate Gross Salary amount."""
    if basic_salary<0 or hra<0 or da<0:
        raise ValueError("Salary amount is negative")
    gross_salary = basic_salary+hra+da

    return{
        "basic_salary": round(basic_salary,2),
        "hra": round(hra,2),
        "da": round(da,2),
        "gross_salary": round(gross_salary,2)
    }