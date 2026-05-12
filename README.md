project-1-data-cleaning-preparation/
│
├── data/
│   ├── dataset.xlsx
│   ├── cleaned_dataset.xlsx
│
├── src/
│   ├── data_cleaning.py
│
├── report/
│   ├── project_report.docx
│
├── README.md
________________________________________
📌 README.md (COPY THIS)
# Project 1: Data Cleaning & Preparation

## 📊 Overview
This project focuses on cleaning and preparing a raw dataset using Python (Pandas).

The goal is to improve data quality by handling missing values, removing duplicates, and standardizing data formats.

---

## 🎯 Objectives
- Identify missing values
- Remove duplicate records
- Correct data formats (dates, numbers, text)
- Prepare dataset for analysis

---

## 🛠 Tools Used
- Python (Pandas, NumPy)
- Excel (for validation)

---

## 📂 Dataset Summary
- Initial rows: 1200  
- Final rows after cleaning: 891  
- Columns: 14  

---

## 🔍 Key Cleaning Steps

### 1. Data Inspection
- Used `df.head()` and `df.info()` to understand dataset structure

### 2. Missing Values
- Identified 309 missing values in CouponCode column
- Removed missing values using `dropna()`

### 3. Duplicate Handling
- Found 11 duplicate CustomerID records
- Removed duplicates to ensure data integrity

### 4. Data Standardization
- Converted date column to datetime format
- Converted numeric fields to proper data types
- Cleaned text fields for consistency

---

## 📊 Result
A clean and structured dataset ready for analysis.

---

## 🚀 How to Run

```bash
pip install pandas numpy openpyxl
python src/data_cleaning.py
________________________________________
👨‍💻 Author
Iyiola Olofin
