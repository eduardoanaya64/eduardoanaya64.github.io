# Eduardo Anaya

IT Business Analyst | Data Analytics | BI & ETL

I’m a data-focused analyst with experience designing and orchestrating ETL pipelines, automating data cleansing workflows, and delivering analytics-ready datasets and dashboards using Power BI, SQL, Python, PostgreSQL, and Apache Airflow.

## Projects

---
### 🧾 Retail Revenue Analytics Pipeline

Snowflake · dbt Cloud · Power BI

Overview

This project demonstrates an end-to-end analytics engineering workflow using Snowflake and dbt Cloud to model retail revenue data from multiple source systems into analytics-ready reporting tables, with Power BI as the consumption layer.

The pipeline integrates Point-of-Sale (POS) transactions and Direct/Billings invoices into a unified revenue model designed for downstream reporting and analytics.

RAW (Snowflake)
 ├─ POS_TRANSACTIONS
 ├─ BILLINGS_INVOICES
     ↓
STAGING (dbt)
 ├─ STG_POS_TRANSACTIONS
 ├─ STG_BILLINGS_INVOICES
     ↓
MARTS (dbt)
 ├─ FCT_REVENUE
 └─ RPT_DAILY_REVENUE
     ↓
Power BI

### Data Modeling Approach

### Raw Layer
- Stores source-aligned data loaded directly from CSV files
- No transformations applied
- Serves as the system of record

### Staging Layer
- Standardizes column naming and data types
- Applies light transformations and casting
- Creates consistent schemas across source systems
- Implemented using dbt models with source references

### Mart Layer
- FCT_REVENUE
  - Unified fact table combining POS and Billings revenue
  - Common grain across revenue channels
- RPT_DAILY_REVENUE
  - Aggregated, reporting-ready table
  - Daily revenue and units by revenue channel

### dbt Features Used
- Sources (sources.yml) to define raw data contracts
- Model references (ref) to enforce dependency order
  - Schema tests:
    - not_null
    - accepted_values
- dbt Cloud runs and builds
- dbt Docs for model documentation and lineage visualization

### Reporting & Consumption (Power BI)
The mart models are designed to act as a semantic layer for BI tools.

### Power BI Integration
- Power BI connects directly to **Snowflake**
- Import mode used for fast, responsive visuals
- Primary dataset:
  RETAIL_DB.STAGING.RPT_DAILY_REVENUE

### Tech Stack
- Snowflake – Cloud data warehouse
- dbt Cloud – Transformations, testing, documentation
- Power BI – Analytics and dashboards

## Data Quality & Testing
- Source-level contracts defined in dbt
- Schema tests enforce:
  - Non-null critical fields
  - Valid revenue channel values
- Models validated using dbt build

### Documentation & Lineage
- dbt Docs generated and hosted in dbt Cloud
- Full lineage graph from RAW → STAGING → MARTS
- Model-level documentation and column descriptions included

### Future Enhancements
- Incremental models for large fact tables
- Data freshness tests
- Dimensional modeling (date, product, customer dimensions)
- Scheduled Power BI refresh
- Additional KPI dashboards

### Why This Project
This project mirrors a real-world analytics engineering workflow, emphasizing:
- Clear separation of raw, staging, and mart layers
- Test-driven transformations
- Analytics-ready outputs
- Scalable design for downstream BI tools

---

### 🚀 Apache Airflow Sales Data Pipeline  

[View Project →](https://github.com/eduardoanaya64/airflow-sales-pipeline)

Built an end-to-end ETL pipeline using Apache Airflow, PostgreSQL, and Docker to ingest, transform, aggregate, and validate sales data across raw, staging, and mart layers.

- Orchestrated multi-step workflow (raw → staging → mart) using PythonOperators  
- Implemented daily incremental loads (idempotent design)  
- Created staging layer with calculated fields (total_amount)  
- Built a mart table with daily sales aggregates  
- Added automated data quality checks (row counts, nulls, negative values)  
- Containerized the entire stack using Docker Compose  
- Visualized pipeline execution in Airflow UI

**Tech:** Python, Apache Airflow, PostgreSQL, Docker, SQL 

### 🧮 Retail Sales Excel Standardization (Python ETL)

Automated a manual Excel cleanup and standardization workflow for retail sales exports using Python.

- Renamed and standardized Excel columns
- Removed unused/internal fields
- Cleaned empty and malformed rows
- Enforced correct data types (dates, currency, quantities)
- Applied consistent Excel formatting using openpyxl

**Tech:** Python, Pandas, Excel  

[View Project →](/projects/retail_excel_etl/)

---

### 📊 Retail POS Analytics Dashboard (Power BI)

Built an interactive retail point-of-sale analytics dashboard using Power BI to analyze sales, profit, customer concentration, product performance, and regional trends across transactional data.

- Designed multi-page interactive dashboard with KPI, trend, customer, product, and regional analysis views
- Modeled POS data to support customer, material (SKU), geographic, and time-based slicing
- Built calculated measures for sales, profit, margin, and period performance comparisons
- Developed time-series visuals to analyze sales and profit trends across reporting periods
- Created ranked customer and product views to identify top revenue and profit contributors
- Implemented regional and state-level mapping visuals to highlight geographic performance patterns
- Enabled dynamic filtering and drill-down using slicers and cross-visual interactions
- Added natural-language Q&A visual to support self-serve business queries
- Optimized dashboard layout and visual density for portfolio-style PDF export and presentation


📄 [View Dashboard (PDF)](POS_Dashboard_Portfolio.pdf)

---



## Tech Stack

**Languages:** Python, SQL  

**Analytics & BI:** Power BI, Tableau, PostgreSQL, Apache Airflow, Docker

**Data:** Excel, CSV, ETL Pipelines, SAP Data Services, Azure Data Factory, AWS Glue

**Systems:** Active Directory, Business Objects  

**Tools:** GitHub, AI-assisted development tools

## Contact
- **LinkedIn:** [https://www.linkedin.com/in/eduardo-anayaa/](https://www.linkedin.com/in/eduardo-anayaa/)
- **Phone:** [714-487-1438](tel:7144871438)
- **Email:** [eduardoanaya64@gmail.com](mailto:eduardoanaya64@gmail.com)

## Resume
👉 [Download My Resume](./Eduardo_Anaya_Resume_2026.pdf)


