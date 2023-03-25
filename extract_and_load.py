import pandas as pd
from sqlalchemy import create_engine
import psycopg2

# Connect to the transactional database
transactional_conn = psycopg2.connect(
    host=os.environ['POSTGRES_HOST'],
    user=os.environ['POSTGRES_USER'],
    password=os.environ['POSTGRES_PASSWORD'],
    dbname=os.environ['POSTGRES_DB']
)

# Connect to the analytics database
analytics_engine = create_engine(f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@{os.environ['POSTGRES_ANALYTICS_HOST']}/{os.environ['POSTGRES_ANALYTICS_DB']}")

# Extract data from all tables in the transactional database
tables = ['table1', 'table2'] # Replace with actual table names
for table in tables:
    df = pd.read_sql(f"SELECT * FROM {table}", transactional_conn)
    df.to_csv(f"/app/extracted_data/{table}.csv", index=False)

# Load data into the analytics database
for table in tables:
    df = pd.read_csv(f"/app/extracted_data/{table}.csv")
    df.to_sql(table, analytics_engine, if_exists='replace', index=False)
