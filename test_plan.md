# Test Plan – MarketDataGuard

## Objective
Ensure stock market datasets across 15 multinational companies meet integrity and logical quality standards.

## Scope
- Validate CSV files sourced from Yahoo Finance API (Jan 2024 – Jan 2026)
- Files include US Tech firms & Indian banking/IT giants

## Test Items
- Data validation engine (validator.py)
- Batch runner (run_validator.py)
- Unit tests (test_validator.py)

## Assumptions
- CSV schema is consistent
- Trading dates follow business calendar
- Volume is non-negative

## Validation Rules
1. Required columns exist  
2. No missing values  
3. Volume >= 0  
4. Prices > 0  
5. High >= Open and Close  
6. Low <= Open and Close  
7. Valid datetime conversion  
8. Dates sorted ascending  
9. No duplicate records  

## Test Types
✔ Unit testing (PyTest)  
✔ Functional dataset testing  
✔ Error logging & reporting  

## Pass/Fail Criteria
- A file passes if **0 errors**
- A file fails if **≥1 rule violation**

## Deliverables
- summary.csv
- error_report.json
- bug_report.md
