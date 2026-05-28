# 📊 Project 1: Data Cleaning & Preprocessing  
## DecodeLabs Internship Program

---

## 👋 Project Overview

This project was completed as part of my **Data Analytics Internship at DecodeLabs**.

The objective was to clean and preprocess a raw transactional dataset using Python (Pandas & NumPy) to ensure the data is accurate, consistent, and analysis-ready.

The dataset contained real-world data quality issues such as missing coupon codes, inconsistent formatting, and pricing validation errors.

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

## 🧾 1. Data Inspection & Standardization

### Observations
- Dataset loaded successfully using Pandas
- Column names standardized to lowercase format

### 💡 Insight
Standardized column names improve consistency and simplify analysis workflows.

---

## ❗ 2. Missing Value Analysis

### Observations
- CouponCode contained **309 missing values**

### 💡 Insight
Missing coupon data reduces visibility into promotional effectiveness and customer discount usage.

---

## 🔄 3. Data Type Correction

### Actions Taken
- Converted `date` column to datetime format  
- Ensured numeric columns were correctly typed  
- Cleaned and standardized text fields  

### 💡 Insight
Proper data types ensure correct calculations and prevent analytical errors.

---

## 🧹 4. Duplicate Check

### Observations
- No duplicate rows were found

### 💡 Insight
The dataset is structurally unique and reliable.

---

## 🏷️ 5. Coupon Code Cleaning

### Issues Identified
- Empty strings  
- "N/A", "NA", "nan" values  

### Action Taken
- Standardized invalid values to maintain consistency

---

## 🧮 6. Business Logic Validation

### Revenue Check
```python
quantity * unitprice == totalprice




---

# 👨‍💻 Author

**Olofin Iyiola Oluwaseun**  
Data Analyst | Python | Power BI | Machine Learning Enthusiast  

📧 Email: olofinio@funaab.edu.ng  

---

# 🔗 Connect With Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Olofin%20Iyiola%20Oluwaseun-blue?style=for-the-badge&logo=linkedin)](www.linkedin.com/in/olofiniyiola)

[![GitHub](https://img.shields.io/badge/GitHub-View%20My%20Projects-black?style=for-the-badge&logo=github)](https://github.com/YOUR-GITHUB-USERNAME)
