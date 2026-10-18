# Brightstone Logistics — Daily Order Reporting Tool

A Python command-line application that transforms CSV order data into daily business reports.

Developed as part of the **Motopp IT Traineeship 2026 — Advanced Python Assignment**.

## Features

- Read order data from a CSV file.
- Validate required columns and order values.
- Calculate the total number of orders and total revenue.
- Identify the top five products by revenue.
- Identify the top five customers by spending.
- Calculate revenue per category, sorted from highest to lowest.
- Export reports in Markdown or JSON format.
- Handle invalid input and file errors with meaningful messages and exit codes.

## Requirements

- Python 3.12 or newer
- pytest and pytest-cov for testing
- mypy for static type checking
- Ruff for linting and formatting

The application itself uses Python's standard library.

## Project Structure

```text
brightstone-report/
├── src/
│   ├── data/
│   │   └── orders.csv
│   └── report/
│       ├── __main__.py
│       ├── cli.py
│       ├── models.py
│       ├── reader.py
│       ├── report.py
│       ├── writer.py
│       └── exceptions.py
├── tests/
├── reports/
├── pyproject.toml
├── .gitignore
└── README.md
```

## Installation

Create and activate a virtual environment.

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install development dependencies:

```powershell
python -m pip install pytest pytest-cov mypy ruff
```

Set the Python source directory:

```powershell
$env:PYTHONPATH = "src"
```

## Usage

Generate a Markdown report:

```powershell
python -m report --input src/data/orders.csv --output reports/daily-report.md --format markdown
```

Generate a JSON report:

```powershell
python -m report --input src/data/orders.csv --output reports/daily-report.json --format json
```

Show command-line help:

```powershell
python -m report --help
```

### CSV Input Format

The input file must contain these columns:

```csv
order_id,date,customer,product,category,quantity,price
1,2026-10-12,John,Laptop,Electronics,2,1250.00
2,2026-10-12,Emma,Mouse,Accessories,1,100.00
```

Each order's revenue is calculated as:

`revenue = quantity * price`

## Testing

Run tests and measure coverage:

```powershell
python -m pytest --cov=report --cov-report=term-missing
```

Latest verified results:

- 23 passing tests
- 88% statement coverage

## Code Quality

Static type checking:

```powershell
python -m mypy --strict src/report
```

Linting:

```powershell
python -m ruff check src/report tests
```

Formatting verification:

```powershell
python -m ruff format --check src/report tests
```

All three checks passed during final verification.

## Architecture

The application separates responsibilities into modules:

- **models.py:** Order and report data structures.
- **reader.py:** CSV parsing and validation.
- **report.py:** Revenue calculations and ranking.
- **writer.py:** Markdown and JSON serialization and file output.
- **cli.py:** Command-line arguments and application orchestration.
- **exceptions.py:** Custom application errors.

This separation makes the reporting calculations independent of the input and output formats.

## Future Improvements

- Support configurable report dates.
- Add additional CLI integration and error-handling tests.
- Use `Decimal` instead of `float` for financial calculations.
- Add automated quality checks through GitHub Actions.

## Author

Developed as an individual assignment for the Motopp IT Traineeship 2026.