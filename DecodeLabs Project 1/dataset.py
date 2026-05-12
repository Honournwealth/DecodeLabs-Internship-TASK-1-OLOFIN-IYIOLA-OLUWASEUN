import pandas as pd
import numpy as np

# =========================
# 0. DISPLAY SETTINGS (EXCEL-LIKE VIEW)
# =========================
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 2000)

# =========================
# 1. LOAD RAW DATASET
# =========================
df = pd.read_excel("dataset.xlsx")

# Standardize column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

print("\n================ RAW DATA INSPECTION ================")

print("\nThis shows the features of the dataset")

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nInitial Dataset Shape:", df.shape)

# =========================
# 2. CHECK DUPLICATES (BEFORE CLEANING)
# =========================
print("\n================ DUPLICATES (BEFORE CLEANING) ================")

duplicate_customers = df.duplicated(subset=["customerid"])

print("Duplicate CustomerIDs (Before Cleaning):",
      duplicate_customers.sum())

print("\nSample Duplicate Rows:")
print(df[duplicate_customers])

# =========================
# 3. CHECK MISSING VALUES (BEFORE CLEANING - EXCEL STYLE)
# =========================
print("\n================ MISSING VALUES (BEFORE CLEANING) ================")

coupon = df["couponcode"]

missing_coupon = coupon.isna() | (coupon.astype(str).str.strip() == "")

print("Missing CouponCode (Excel-like COUNTBLANK):",
      missing_coupon.sum())

print("\nMissing Values Per Column:")
print(df.isnull().sum())

# =========================
# 4. DATA TYPE CORRECTION
# =========================
print("\n================ DATA TYPE CORRECTION ================")

df["date"] = pd.to_datetime(df["date"], errors="coerce")

df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
df["unitprice"] = pd.to_numeric(df["unitprice"], errors="coerce")
df["totalprice"] = pd.to_numeric(df["totalprice"], errors="coerce")

text_cols = [
    "orderid", "customerid", "couponcode",
    "referralsource", "paymentmethod",
    "orderstatus", "shippingaddress", "product"
]

for col in text_cols:
    df[col] = df[col].astype(str).str.strip()

# =========================
# 5. CLEAN COUPONCODE COLUMN
# =========================
print("\n================ CLEANING COUPONCODE ================")

df["couponcode"] = df["couponcode"].replace(
    ["", " ", "N/A", "NA", "-", "nan"],
    np.nan
)

# =========================
# 6. DROP MISSING VALUES
# =========================
print("\n================ DROPPING MISSING VALUES ================")

df_clean = df.dropna()

print("Dataset Shape After Dropna:", df_clean.shape)

# =========================
# 7. CHECK DUPLICATES AFTER CLEANING
# =========================
print("\n================ DUPLICATES (AFTER CLEANING) ================")

dup_after = df_clean.duplicated(subset=["customerid"])

print("Duplicate CustomerIDs (After Cleaning):",
      dup_after.sum())

df_clean = df_clean.drop_duplicates(subset=["customerid"])

print("Final Duplicate CustomerIDs Left:",
      df_clean.duplicated(subset=["customerid"]).sum())

# =========================
# 8. BUSINESS LOGIC VALIDATION
# =========================
print("\n================ BUSINESS LOGIC VALIDATION ================")

df_clean["calculated_total"] = df_clean["quantity"] * df_clean["unitprice"]

mismatch = df_clean[df_clean["totalprice"] != df_clean["calculated_total"]]

print("Mismatched TotalPrice rows:", len(mismatch))

df_clean.drop(columns=["calculated_total"], inplace=True)

# =========================
# 9. FINAL DATA CHECK
# =========================
print("\n================ FINAL CLEAN DATA CHECK ================")

print("\nMissing Values After Cleaning:")
print(df_clean.isnull().sum())

print("\nFinal Dataset Shape:", df_clean.shape)

print("\nCleaned Dataset Preview:")
print(df_clean.head())

# =========================
# 10. SAVE CLEANED DATASET
# =========================
df_clean.to_excel("cleaned_dataset.xlsx", index=False)

print("\nCleaned dataset saved successfully!")