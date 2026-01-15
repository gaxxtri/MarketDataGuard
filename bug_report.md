# Bug Report Log – MarketDataGuard

## Overview
Validation errors detected across multiple stock datasets while executing automated checks.

| File                 | Rule Failed                | Rows/Details                             | Severity |
|---------------------|----------------------------|------------------------------------------|----------|
| AAPL.csv            | missing_values             | Volume missing at index 122              | Medium   |
| Tesla.csv           | non_positive_prices        | Open <= 0 at index 15                    | High     |
| Google.csv          | price_bound_violation      | High < Close at index 78                 | High     |
| Microsoft.csv       | duplicate_rows             | Duplicate detected at index 200          | Low      |
| Infosys.csv         | unsorted_dates             | Dates not ascending after 2025-08-14     | Medium   |

## Notes
- All errors detected and logged using automated validation engine.
- Further cleaning or dataset preprocessing required prior to modeling.
