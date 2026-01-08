# Retail Sales Excel Standardization (Python ETL)

## Overview
This project demonstrates how a manual Excel cleanup and formatting process can be automated using Python.  
The pipeline transforms raw, vendor-style Excel exports into clean, standardized, and analysis-ready workbooks suitable for downstream ETL and reporting.

⚠️ **All data in this project is synthetic.**  
Column names, values, and files were intentionally fabricated to preserve confidentiality while maintaining realistic structure and complexity.

---

## Problem
Weekly retail sales exports often arrive as raw Excel files with:

- Inconsistent column names and ordering
- Internal or unused fields mixed with business data
- Dates and currency stored as plain text
- Blank or malformed rows
- Manual formatting requirements before loading into reporting systems

This manual cleanup process is time-consuming and error-prone.

---

## Solution
I built a Python-based ETL-style workflow that:

- Mimics real-world vendor Excel exports
- Applies deterministic, repeatable transformation logic
- Outputs standardized Excel files ready for analytics or database ingestion

---

## Pipeline Flow

Synthetic Vendor Export (Excel)
↓
Python Transformation (pandas)
↓
Standardized Excel Output
↓
(Representative of downstream ETL / BI workflows)


---

## Key Processing Steps

### 1. Column Standardization
- Renames columns based on documented manual steps:
  - Column **B → Unit Name**
  - Column **D → Description**
- Removes unused or internal columns:
  - Column **F**
  - Column **J**

---

### 2. Data Cleaning
- Drops fully empty rows
- Removes malformed or invalid records
- Preserves rows containing meaningful business data

---

### 3. Type Enforcement
- Converts date-like fields to proper `datetime` objects
- Converts currency strings (e.g. `$1,234.56`) to numeric values
- Ensures quantity fields are numeric for aggregation and validation

---

### 4. Output Formatting
- Renames worksheet to a standardized report name
- Removes all borders and bold formatting
- Applies consistent number formats:
  - Dates → `M/D/YYYY`
  - Currency → `$#,##0.00`
  - Quantities → whole numbers

Formatting is applied using **openpyxl** to ensure Excel compatibility.

---

## Example Columns (Synthetic)

| Column Name     | Description                       |
|-----------------|-----------------------------------|
| Unit Name       | Store or location identifier      |
| Description     | Product description               |
| Report Date     | Transaction date                  |
| Sales: $        | Sales amount (currency)           |
| Sales: Qty      | Units sold                        |
| Region          | Sales region                      |
| Channel         | Sales channel                     |

---

## Repository Structure

projects/retail_excel_etl/
├── README.md
├── generator_fake_meijer_export.py
├── processor_fake_meijer_export.py
└── images/


---

## How to Run

### 1. Generate Synthetic Raw Exports
Creates fake vendor-style Excel files for testing.

```bash
python generator_fake_meijer_export.py
