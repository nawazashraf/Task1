# 🚗 Vehicle Sales Data Cleaning Project

This project involves cleaning and preprocessing a real-world vehicle sales dataset to make it suitable for analysis, visualization, or machine learning applications.

---

## 📁 Dataset Overview

**Original Columns:**

- `year`, `make`, `model`, `trim`, `body`, `transmission`, `vin`, `state`, `condition`, `odometer`, `color`, `interior`, `seller`, `mmr`, `sellingprice`, `saledate`

**Source**: Public dataset downloaded from Kaggle.

---

## 🧼 Cleaning Process

The following data cleaning steps were performed using Python and Pandas:

### 🔹 1. Handled Missing Values
- Removed rows with missing critical fields like `vin`, `sellingprice`, and `saledate`.
- Filled missing categorical values with placeholders (`'unknown'`, `'standard'`, etc.).
- Filled missing numeric fields (`odometer`, `mmr`) using the **median**.
- Filled `condition` using the **mode**.

### 🔹 2. Removed Duplicates
- Used `.drop_duplicates()` to eliminate redundant records.

### 🔹 3. Standardized Text Values
- Cleaned and standardized string columns (e.g. `make`, `model`, `transmission`, etc.) by converting them to lowercase and stripping whitespace.
- Normalized inconsistent terms in `transmission` and `condition`.

### 🔹 4. Converted Date Format
- Parsed the `saledate` column to a consistent `datetime64[ns, UTC]` format.
- Optional: Converted date to `dd-mm-yyyy` string format (for display/export purposes).

### 🔹 5. Renamed Columns
- All column headers were cleaned to lowercase with underscores (`_`) instead of spaces for consistency.

### 🔹 6. Fixed Data Types
- Ensured that numeric columns (`year`, `condition`, `odometer`, `mmr`, `sellingprice`) have appropriate types (`int` or `float`).
- Confirmed that `saledate` is stored in a proper datetime format.

---

## 📦 Output

- `vehicle_sales_cleaned.csv` — Final cleaned CSV file
- `vehicle_sales_cleaned.xlsx` — Cleaned dataset in Excel format (optional)

---

## 🛠️ Tools Used

- Python
- Pandas
- Jupyter Notebook / VS Code
- OpenPyXL (for `.xlsx` export)

---


## 📝 License

This project is licensed under the [MIT License](LICENSE) - feel free to use and modify.

