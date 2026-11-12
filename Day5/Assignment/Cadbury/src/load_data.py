import pandas as pd

def load_all_data(data_dir):
  """Read the 3 CSV files and return them."""
  sales = pd.read_csv(data_dir / "Cadbury_Dairy_Milk_Sales_2025_Synthetic.csv")
  products = pd.read_csv(data_dir / "Cadbury_Product_Master.csv")
  stores = pd.read_csv(data_dir / "Cadbury_Store_Master.csv")
  print("Sales:", sales.shape)
  print("Products:", products.shape)
  print("Stores:", stores.shape)

  return sales, products, stores