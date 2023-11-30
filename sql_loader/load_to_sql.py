import pandas as pd
import sqlalchemy
from sql_config import SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DB

# Create SQL engine
engine = sqlalchemy.create_engine(f'mysql+pymysql://{SQL_USER}:{SQL_PASSWORD}@{SQL_HOST}/{SQL_DB}')

# Load CSV data
df = pd.read_csv('path_to_your_csv_file.csv')

# Load data into SQL
df.to_sql('yellow_taxi_data', con=engine, if_exists='replace', index=False)
