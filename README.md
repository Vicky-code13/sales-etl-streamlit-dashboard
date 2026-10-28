# Sales ETL Pipeline & Streamlit Dashboard

A Python-based Sales ETL Pipeline that extracts, cleans, transforms, and validates sales data, with an interactive Streamlit dashboard for exploring sales performance and business KPIs.

## Project Overview

This project demonstrates how raw sales data can be processed into structured, analysis-ready data and presented through an interactive dashboard. It combines Python-based data processing with data visualization to support business reporting and decision-making.

## Key Features

- **Data Extraction:** Load sales data from source files.
- **Data Cleaning:** Handle missing values, inconsistent data, and formatting issues.
- **Data Transformation:** Filter, aggregate, and transform sales records using Pandas.
- **Data Validation:** Perform checks to improve data consistency and reliability.
- **Sales Analysis:** Analyze sales performance and product-level metrics.
- **Interactive Dashboard:** Explore key performance indicators and sales insights using Streamlit.
- **Modular Structure:** Organize configuration, database-related code, scripts, data, and dashboard components into separate directories.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming and ETL logic |
| Pandas | Data cleaning, transformation, and analysis |
| Streamlit | Interactive dashboard |
| SQL | Database querying, where configured |
| Git & GitHub | Version control and project hosting |

## Project Structure

```text
sales-etl-streamlit-dashboard/
│
├── config/          # Configuration files
├── data/            # Source or processed datasets
├── database/        # Database-related components
├── img/             # Images and dashboard assets
├── scripts/         # Supporting scripts
├── analysis.txt     # Analysis notes
├── main.py          # Main ETL entry point
├── dashboard.py     # Streamlit dashboard
└── README.md        # Project documentation
```

## ETL Workflow

1. **Extract** — Read sales data from the configured source.
2. **Transform** — Clean records, standardize data, and perform required calculations.
3. **Validate** — Check the processed data for consistency and quality.
4. **Analyze** — Calculate sales metrics and product-level performance.
5. **Visualize** — Present the results in an interactive Streamlit dashboard.

## Getting Started

### Prerequisites

- Python 3.10 or later (use a version compatible with your installed dependencies)
- pip
- Git

### 1. Clone the repository

```bash
git clone https://github.com/Vicky-code13/sales-etl-streamlit-dashboard.git
```

### 2. Navigate to the project directory

```bash
cd sales-etl-streamlit-dashboard
```

### 3. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

If the project includes a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Otherwise, install the required libraries based on your imports. For example:

```bash
pip install pandas streamlit
```

Install any additional database drivers or libraries required by your implementation.

### 5. Run the ETL pipeline

```bash
python main.py
```

### 6. Launch the dashboard

```bash
streamlit run dashboard.py
```

Streamlit will provide a local URL in your terminal. Open that URL in your browser to access the dashboard.

**Note:** Update the commands or dependencies if your current implementation uses a different entry point or setup.

## Expected Outcomes

- Structured and analysis-ready sales data.
- Improved consistency through data cleaning and validation.
- Sales and product performance insights.
- An interactive interface for exploring business metrics.

## Skills Demonstrated

- Python programming
- Data processing with Pandas
- ETL pipeline development
- Data cleaning and validation
- SQL and database concepts
- Business data analysis
- Interactive dashboard development
- Project organization and version control

## Future Improvements

- Automate scheduled ETL execution.
- Add structured logging and error handling.
- Implement automated data quality tests.
- Integrate additional data sources.
- Deploy the Streamlit dashboard to a cloud platform.

## Author

**Vignesh S**

GitHub: [Vicky-code13](https://github.com/Vicky-code13)

---

*This project was developed for hands-on practice in sales data processing, ETL workflow design, and interactive business analytics.*
