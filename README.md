# 🧹 Project 1: Data Cleaning & Preprocessing  
## DecodeLabs Internship Program

---

## 👋 Project Overview

This project was completed as part of my **Data Analytics Internship at DecodeLabs**.

The objective was to clean and preprocess a raw transactional dataset using Python (Pandas & NumPy) to ensure data accuracy, consistency, and readiness for analysis.

The dataset contained real-world data quality issues such as missing values in coupon codes and business logic inconsistencies in pricing.

---

## 📂 Dataset Overview

- Total Rows (Before Cleaning): **1200**
- Total Rows (After Cleaning): **891**
- Total Columns: **14**

### Key Features
- Order ID  
- Customer ID  
- Product  
- Quantity  
- Unit Price  
- Total Price  
- Payment Method  
- Coupon Code  
- Order Status  
- Referral Source  
- Shipping Address  
- Date  

---

# 🧹 Data Cleaning Process

---

## 1. Data Inspection & Standardization

### Actions Performed:
- Loaded dataset using Pandas  
- Standardized column names (lowercase, underscore format)  
- Inspected dataset structure and data types  

### Insight:
Consistent formatting improves readability and ensures smooth data processing.

---

## 2. Missing Value Analysis

### Findings:
- CouponCode column had **309 missing values**

### Action Taken:
- Missing and invalid coupon values were standardized and removed during cleaning

### Insight:
Missing coupon data may impact marketing and customer behavior analysis.

---

## 3. Data Type Correction

### Actions:
- Converted `date` column to datetime format  
- Ensured numeric fields (quantity, unitprice, totalprice) were correctly typed  
- Cleaned text fields by stripping extra spaces  

### Insight:
Correct data types ensure accurate calculations and aggregations.

---

## 4. Duplicate Check

### Findings:
- No full-row duplicates were detected

### Insight:
The dataset maintained strong structural uniqueness.

---

## 5. Coupon Code Cleaning

### Issues Identified:
- Empty strings, "N/A", and inconsistent entries

### Solution:
- Standardized invalid entries to proper missing values before cleaning

---

## 6. Missing Value Removal

### Result:
- Dataset reduced from **1200 → 891 rows**

### Insight:
Although data loss occurred, it improved overall dataset reliability.

---

## 7. Business Logic Validation

### Check Performed:
```python
quantity * unitprice == totalprice
