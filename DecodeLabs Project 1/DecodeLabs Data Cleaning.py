import pandas as pd
import numpy as np

# =========================
# 0. DISPLAY SETTINGS
# =========================
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 2000)

# =========================
# 1. LOAD DATASET
# =========================
df = pd.read_excel("dataset.xlsx")

# Standardize column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

print("\n================ RAW DATA INSPECTION ================")

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nInitial Dataset Shape:", df.shape)

# =========================
# 2. CHECK FULL ROW DUPLICATES
# =========================
print("\n================ FULL ROW DUPLICATES (BEFORE CLEANING) ================")

full_duplicates = df.duplicated()

print("Total Full Row Duplicates:",
      full_duplicates.sum())

print("\nSample Duplicate Rows:")
print(df[full_duplicates])

# =========================
# 3. CHECK MISSING VALUES
# =========================
print("\n================ MISSING VALUES (BEFORE CLEANING) ================")

coupon = df["couponcode"]

missing_coupon = coupon.isna() | (
    coupon.astype(str).str.strip() == ""
)

print("Missing CouponCode (Excel-like COUNTBLANK):",
      missing_coupon.sum())

print("\nMissing Values Per Column:")
print(df.isnull().sum())

# =========================
# 4. DATA TYPE CORRECTION
# =========================
print("\n================ DATA TYPE CORRECTION ================")

# Convert date column
df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)

# Convert numeric columns
df["quantity"] = pd.to_numeric(
    df["quantity"],
    errors="coerce"
)

df["unitprice"] = pd.to_numeric(
    df["unitprice"],
    errors="coerce"
)

df["totalprice"] = pd.to_numeric(
    df["totalprice"],
    errors="coerce"
)

# Clean text columns
text_cols = [
    "orderid",
    "customerid",
    "couponcode",
    "referralsource",
    "paymentmethod",
    "orderstatus",
    "shippingaddress",
    "product",
    "trackingnumber"
]

for col in text_cols:
    df[col] = (
        df[col]
        .astype(str)
        .str.strip()
    )

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

print("Dataset Shape After Dropna:",
      df_clean.shape)

# =========================
# 7. REMOVE FULL ROW DUPLICATES
# =========================
print("\n================ REMOVING FULL ROW DUPLICATES ================")

duplicates_after_cleaning = df_clean.duplicated()

print("Full Row Duplicates Remaining:",
      duplicates_after_cleaning.sum())

# Remove full duplicate rows
df_clean = df_clean.drop_duplicates()

print("Duplicates Left After Removal:",
      df_clean.duplicated().sum())

# =========================
# 8. BUSINESS LOGIC VALIDATION
# =========================
print("\n================ BUSINESS LOGIC VALIDATION ================")

df_clean["calculated_total"] = (
    df_clean["quantity"] *
    df_clean["unitprice"]
)

mismatch = df_clean[
    df_clean["totalprice"] !=
    df_clean["calculated_total"]
]

print("Mismatched TotalPrice Rows:",
      len(mismatch))

# Remove temporary column
df_clean.drop(
    columns=["calculated_total"],
    inplace=True
)

# =========================
# 9. FINAL DATA CHECK
# =========================
print("\n================ FINAL CLEAN DATA CHECK ================")

print("\nMissing Values After Cleaning:")
print(df_clean.isnull().sum())

print("\nFinal Dataset Shape:",
      df_clean.shape)

print("\nCleaned Dataset Preview:")
print(df_clean.head())

# =========================
# 10. SAVE CLEANED DATASET
# =========================
df_clean.to_excel(
    "cleaned_dataset.xlsx",
    index=False
)

print("\nCleaned dataset saved successfully!")