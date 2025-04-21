import pandas as pd
import os
from sqlalchemy import create_engine

# Paths
base_path = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(base_path, "input_data", "vehicle_loan_data.csv")
db_path = os.path.join(base_path, "vehicle_loans.db")

# Read CSV
df = pd.read_csv(input_file)

# Connect to SQLite
engine = create_engine(f"sqlite:///{db_path}", echo=False)

# Save to database
df.to_sql("vehicle_loans", con=engine, if_exists="replace", index=False)

print("✅ Vehicle loan data loaded into 'vehicle_loans.db' SQLite database.")
