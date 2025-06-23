# Import pandas library for data manipulation and analysis
import pandas as pd

# Loaded the dataset from CSV file into a DataFrame
df = pd.read_csv("car_prices.csv")

# Display the DataFrame to inspect initial data
df

# Checking for missing values in each column
df.isnull().sum()

# DATA CLEANING SECTION

# Dropped the rows with missing values in critical columns (vin, sellingprice, saledate)
df = df.dropna(subset=['vin', 'sellingprice', 'saledate']).copy()

# Filled missing numerical values with median (odometer and mmr columns)
df.loc[:, 'odometer'] = df['odometer'].fillna(df['odometer'].median())
df.loc[:, 'mmr'] = df['mmr'].fillna(df['mmr'].median())

# Filled missing categorical values with appropriate placeholders
df.loc[:, 'model'] = df['model'].fillna('unknown')
df.loc[:, 'make'] = df['make'].fillna('unknown')
df.loc[:, 'trim'] = df['trim'].fillna('standard')
df.loc[:, 'body'] = df['body'].fillna('unknown')
df.loc[:, 'color'] = df['color'].fillna('unknown')
df.loc[:, 'interior'] = df['interior'].fillna('unknown')
df.loc[:, 'transmission'] = df['transmission'].fillna('unknown')
# For condition, filled with the most frequent value (mode)
df.loc[:, 'condition'] = df['condition'].fillna(df['condition'].mode()[0])

# Checking for duplicate rows in the DataFrame
df.duplicated().sum()

# Remove duplicate rows from the DataFrame
df = df.drop_duplicates()

# DATA STANDARDIZATION SECTION

# Standardize text columns: convert to lowercase and remove leading/trailing whitespace
for col in ['make', 'model', 'trim', 'body', 'transmission', 'state', 'color', 'interior', 'seller']:
    df[col] = df[col].str.lower().str.strip()

# Convert saledate to datetime format with UTC timezone
df['saledate'] = pd.to_datetime(
    df['saledate'], 
    format='%Y-%m-%d %H:%M:%S%z', 
    errors='coerce', 
    utc=True
)

# Standardize column names: lowercase, strip whitespace, replace spaces with underscores
df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')

# Check data types of all columns to ensure proper formatting
df.dtypes

# EXPORT CLEANED DATA

df.to_excel('vehicle_sales_cleaned.xlsx', index=False, engine='openpyxl')