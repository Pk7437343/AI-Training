from pathlib import Path
import sqlite3
import pandas as pd
 
 
BASE_DIR=Path(__file__).resolve().parent
 
print(f"Base directory :{BASE_DIR}")
 
DATA_DIR=BASE_DIR/"data"
REPORT_DIR=BASE_DIR/"report"
DATABASE_DIR=BASE_DIR/"database"
 
print(f"Data directory :{DATA_DIR}")
print(f"Report directory :{REPORT_DIR}")
print(f"Database directory : {DATABASE_DIR}")
 
#DATABASE_PATH=DATABASE_DIR/"ecommerce_warehouse.db"

def create_folders()-> None:
    """create report and database folders if they dont exist"""
    REPORT_DIR.mkdir(exist_ok=True)
    DATABASE_DIR.mkdir(exist_ok=True)

def extract_data() -> tuple[
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame
]:
    """read data from csv files"""
    customers = pd.read_csv(
        DATA_DIR / "customers.csv",
        encoding="utf-8-sig"
    )

    orders = pd.read_csv(
        DATA_DIR / "orders.csv",
        encoding="utf-8-sig"  
    )

    payments = pd.read_csv(
        DATA_DIR / "payments.csv",
        encoding="utf-8-sig"
    )

    deliveries = pd.read_csv(
        DATA_DIR / "deliveries.csv",
        encoding="utf-8-sig"
    )

    for dataframe in [
        customers,
        orders,
        payments,
        deliveries
        
    ]:
        dataframe.columns = (
            dataframe.columns.astype(str)
            .str.replace("\ufeff", "", regex=False)
            .str.strip()
            .str.lower()
        )

    print("Customer column:", customers.columns.tolist())
    print("orders column:", orders.columns.tolist())
    print("payments column", payments.columns.tolist())
    print("delivery column", deliveries.columns.tolist())
extract_data();

def clean_customers(customers: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicates"""

    customers = customers.copy()
    customers = customers.drop_duplicates(
        subset=["customer_id"]
    )

    customers["customer_name"] =(
        customers["customers_name"]
        .fillna("Unknown Customer")
        .astype(str)
        .str.strip()
        .str.title()
    )
    customers["customer_email"] = (
        customers["email"]
        .fillna("Unknown@gmail.com")
        .astype(str)
        .str.strip()
        .str.title()
    )

    customers["city"] = (
        customers["city"]
        .fillna("unknown")
        .astype(str)
        .str.strip()
        .str.lower()
    )

    return customers
##-------------------------



def clean_orders(orders:pd.DataFrame) -> pd.DataFrame:
    orders = orders.copy()
    orders = orders.drop_duplicates(
        subset=["order_id"]
        )
    # orders = orders.drop_duplicates(
    #         subset=["customer_id"]
    #     )
   
    orders = orders["product_name"]=(
        orders["product_name"]
        .fillna("unknown product")
        .astype(str)
        .str.strip()
        .str.title()
    )
   
    orders["quantity"] = pd.to_numeric(
        orders["quantity"],
        errors="coerce"
    ).fillna(0)
   
    orders["unit_price"] = pd.to_numeric(
        orders["unit_price"],
        errors=  "coerce"
    ).fillna(0)
   
    orders["order_date"]= pd.to_datetime(
        orders["order_date"],
        errors="coerce"
    )
   
    orders["total_amount"] = (
        orders["quantity"] + orders["unit_price"]
    )
    return orders
   
       
 ##------------

def clean_payments(payments:pd.DataFrame) -> pd.DataFrame:
    payments = payments.copy()
    payments = payments.drop_duplicates(
        subset=["payment_id"]
        )
   
    payments = payments["payment_status"]=(
        payments["payment_status"]
        .fillna("unknown product")
        .astype(str)
        .str.strip()
        .str.title()
    )
   
    payments = payments["payment_method"]=(
            payments["payment_status"]
            .fillna("unknown product")
            .astype(str)
            .str.strip()
            .str.title()
        )
   
    payments["payment_date"]= pd.to_datetime(
            payments["payment_date"],
            errors="coerce"
        )
   
    return payments      
       


def clean_deliveries(deliveries:pd.DataFrame) -> pd.DataFrame:
    deliveries = deliveries.copy()
    deliveries = deliveries.drop_duplicates(
        subset=["delivery_id"]
        )
    # deliveries = deliveries.drop_duplicates(
    #         subset=["order_id"]
    #     )
   

   
    deliveries = deliveries["delivery_status"]=(
            deliveries["delivery_status"]
            .fillna("unknown product")
            .astype(str)
            .str.strip()
            .str.title()
        )
   
    deliveries = deliveries["delivery_city"]=(
                deliveries["delivery_city"]
                .fillna("unknown product")
                .astype(str)
                .str.strip()
                .str.title()
            )
    return deliveries  
def join_data(
        customers: pd.DataFrame,
        orders: pd.DataFrame,
        payments: pd.DataFrame,
        deliveries: pd.DataFrame
) -> pd.DataFrame:
    """join customers, orders, payments and deliveries"""
    combined_data = orders.merge(
        customers,
        on="customer_id"
        how="left"
    )

    combined_data = orders.merge(
            customers,
            on="customer_id"
            how="left"
        )
    combined_data = orders.merge(
            payments,
            on="order_id"
            how="left"
        )

    combined_data = orders.merge(
            deliveries,
            on="orders_id"
            how="left"
        )


    
    combined_data["customer_name"]= (
        combined_data["customer_name"]
        .filna("unknown")
    )

    combined_data["city"]= (
        combined_data["city"]
        .filna("unknown")
    )
    
    combined_data["payment_status"]= (
        combined_data["payment_status"]
        .filna("unknown")
    ) 

    combined_data["delivery_status"]= (
        combined_data["delivery_status"]
        .filna("unknown")
    )           

def generate_total_orders_report(combined_data: pd.DataFrame) -> pd.DataFrame:




def generate_total_reveneue_report(combined_data: pd.DataFrame) -> pd.DataFrame:
    """calc revenue"""

    successful_orders = combined_data[
        combined_data["payment_status"]== "success"
    ]
    total_revenue = 
    





































































# from pathlib import Path
# import sqlite3
# import pandas as pd
 
# BASE_DIR = Path(__file__).resolve().parent
# print(f"Base directory: {BASE_DIR}")
 
# DATA_DIR = BASE_DIR /"data"
# REPORT_DIR = BASE_DIR /"reports"
# DATABASE_DIR = BASE_DIR /"database"
# print(f"Data directory: {DATA_DIR}")
# print(f"report directory: {REPORT_DIR}")
# print(f"database directory: {DATABASE_DIR}")
 
# DATABASE_PATH = DATA_DIR / "ecoomerce_warehous.db"
# print(f"database path: {DATABASE_PATH}")
 
# def create_folders() -> None:
#     """create report and database folders if they do no exist"""
   
#     REPORT_DIR.mkdir(exist_ok=True)
#     DATABASE_DIR.mkdir(exist_ok=True)
   
   
   
# def extract_data() -> tuple[
#     pd.DataFrame,
#     pd.DataFrame,
#     pd.DataFrame,
#     pd.DataFrame
# ]:
   
   
#     customers = pd.read_csv(
#         DATA_DIR / "customers.csv",
#         encoding="utf-8-sig"
#     )
   
#     payments = pd.read_csv(
#         DATA_DIR / "payments.csv",
#         encoding="utf-8-sig"
 
#     )
   
#     deliveries = pd.read_csv(
#         DATA_DIR/ "deliveries.csv",
#         encoding="utf-8-sig"
 
#     )
   
#     orders = pd.read_csv(
#         DATA_DIR / "orders.csv",
#         encoding="utf-8-sig"
 
#     )
 
#     for dataframe in [
#         customers,
#         payments,
#         deliveries,
#         orders
#     ]:
#         dataframe.columns =(
#             dataframe.columns
#             .astype(str)
#             .str.replace("\ufeff", "", regex=False)
#             .str.strip()
#             .str.lower()
#         )
 
#     print("Customers columns ", customers.columns.tolist())
#     print("Order columns ", orders.columns.tolist())
#     print("payment columns ", payments.columns.tolist())
#     print("delivery columns", deliveries.columns.tolist())
   
#     return customers, orders,payments,deliveries
# extract_data()
 
# def clean_customers(customers:pd.DataFrame) -> pd.DataFrame:
#     customers = customers.copy()
#     customers = customers.drop_duplicates(
#         subset=["customer_id"]
#     )
   
#     customers["customer_name"] =(
#         customers["customers_name"]
#         .fillna("unknown customers")
#         .astype(str)
#         .str.strip()
#         .str.title()
#     )
   
#     customers["email"] =(
#         customers["email"]
#         .fillna("unknown@gmail.com")
#         .astype(str)
#         .str.strip()
#         .str.title()
#     )
#     customers["city"] = (
#         customers["city"]
#         .fillna("unknown")
#         .astype(str)
#         .str.strip()
#         .str.title()
 
#     )
   
#     return customers
 
# def clean_orders(orders:pd.DataFrame) -> pd.DataFrame:
#     orders = orders.copy()
#     orders = orders.drop_duplicates(
#         subset=["order_id"]
#         )
#     orders = orders.drop_duplicates(
#             subset=["customer_id"]
#         )
   
#     orders = orders["product_name"]=(
#         orders["product_name"]
#         .fillna("unknown product")
#         .astype(str)
#         .str.strip()
#         .str.title()
#     )
   
#     orders["quantity"] = pd.to_numeric(
#         orders["quantity"],
#         errors="coerce"
#     ).fillna(0)
   
#     orders["unit_price"] = pd.to_numeric(
#         orders["unit_price"],
#         errors=  "coerce"
#     ).fillna(0)
   
#     orders["order_date"]= pd.to_datetime(
#         orders["order_date"],
#         errors="coerce"
#     )
   
#     orders["total_amount"] = (
#         orders["quantity"] + orders["unit_price"]
#     )
#     return orders
   
       
       
# def clean_payments(payments:pd.DataFrame) -> pd.DataFrame:
#     payments = payments.copy()
#     payments = payments.drop_duplicates(
#         subset=["payment_id"]
#         )
#     payments = payments.drop_duplicates(
#             subset=["order_id"]
#         )
   
#     payments = payments["payment_status"]=(
#         payments["payment_status"]
#         .fillna("unknown product")
#         .astype(str)
#         .str.strip()
#         .str.title()
#     )
   
#     payments = payments["payment_method"]=(
#             payments["payment_status"]
#             .fillna("unknown product")
#             .astype(str)
#             .str.strip()
#             .str.title()
#         )
   
#     payments["payment_date"]= pd.to_datetime(
#             payments["payment_date"],
#             errors="coerce"
#         )
   
#     return payments      
       
       
       
