CSV CLEANER (CLI)

A Python command-line tool to clean and normalize CSV files.
Designed for data preprocessing, automation, and Excel/pandas workflows.

---

FEATURES

- Remove duplicate rows
- Drop empty rows
- Normalize column names
- Export cleaned CSV
- Simple CLI interface

---

PROJECT STRUCTURE

csv-cleaner/
|
|-- csv_cleaner/        Core package
|   |-- cli.py          CLI parsing
|   |-- cleaner.py      Cleaning logic
|
|-- examples/           Sample input/output
|-- tests/              Unit tests (future)
|-- main.py             Entry point
|-- requirements.txt
|-- README.md
|-- README.txt

---

INSTALLATION

git clone https://github.com/<your-username>/csv-cleaner.git
cd csv-cleaner
python -m pip install -r requirements.txt

---

USAGE

python main.py examples/dirty_data.csv

With options:

python main.py examples/dirty_data.csv --drop-empty --dedup --normalize-cols

Output:
examples/dirty_data_cleaned.csv

---

CLI OPTIONS

--drop-empty         Remove empty rows
--dedup              Remove duplicates
--normalize-cols     Normalize column names
-o, --output         Custom output path
--encoding           CSV encoding (default: utf-8)

---

EXAMPLE

Input:

Name,Email, Age ,City
Alice,alice@example.com,25,Montreal
Bob,bob@example.com, ,Quebec
Bob,bob@example.com, ,Quebec

,,,
Charlie,charlie@example.com,30,Montreal

Output:

name,email,age,city
Alice,alice@example.com,25,Montreal
Bob,bob@example.com,,Quebec
Charlie,charlie@example.com,30,Montreal

---

AUTHOR

Michel Brochu
Python | Automation | Data Tools

---

LICENSE

MIT (or later)
