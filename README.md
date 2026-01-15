# 📊 MarketDataGuard – Data Quality Scanner for Financial Datasets

As data scientists, we love building models, forecasting trends, and telling stories with data —  
but there's one step we quietly struggle with every single time:

**DATA CLEANING.**

Stock datasets downloaded from Yahoo Finance or APIs *look* clean, but beneath the surface they often hide:
- ❌ Missing values
- ❌ Wrong price relationships (High < Close??)
- ❌ Negative or impossible numbers
- ❌ Duplicate rows
- ❌ Unsorted or invalid dates
- ❌ Columns that silently break

These issues destroy pipelines, distort predictions, and eat hours of debugging time.

So I built **MarketDataGuard** — a lightweight validation engine that checks stock price datasets before they enter your notebook or ML pipeline.

---

## 🚀 What MarketDataGuard Does

This tool runs systematic checks across all CSV files and automatically flags violations such as:

✔ Missing or null values  
✔ Negative prices or volume  
✔ Prices breaking financial rules  
✔ Non-monotonic dates  
✔ Bad formats  
✔ Duplicate rows  

It then:
📌 Logs all issues  
📌 Generates a CSV summary  
📌 Outputs a JSON error report  
📌 And gives a clear PASS/FAIL per dataset

No more guessing. No more silent errors.

---

## 💡 Why This Matters

### For Data Scientists
Clean input → Better models.  
Data issues caught early → Less work later.  
This tool ensures your ARIMA, LSTM, or regression models are fed trustworthy data.

### For Software Quality Engineers
This project mirrors real QA pipelines:
- Rule-based logic
- Automated execution
- Reproducible results
- Unit testing
- Test plan + bug log
- Reporting artifacts

It’s testing discipline, applied to data.

---

## 📁 Project Structure
MarketDataGuard/
├── data/ <- Raw company CSVs
├── reports/ <- JSON + CSV outputs
├── src/
│ ├── validator.py <- validation rules
│ └── run_validator.py <- batch executor + reporting
├── tests/ <- Unit tests with PyTest
├── bug_report.md <- Human-readable defect summary
├── test_plan.md <- Test design & rules
├── README.md <- This file
└── requirements.txt


---

## ⚙️ How to Run

pip install -r requirements.txt
reports/error_report.json → errors logged
reports/summary.csv → count of issues
bug_report.md → human readable list

---

##Future Enhancements

Auto-cleaning and repair suggestions

Data quality scoring (0–100)

Outlier and anomaly checks

Integration into training pipelines

Small UI or CLI frontend

✨ Why I Built This

I believe data science should start with truth, not assumptions.
Bad data creates bad decisions.
MarketDataGuard lets me trust the input so I can focus on insights — not errors.

This project reflects what I care about:
✔ Data quality
✔ Testing discipline
✔ Reliable pipelines
✔ Building tools that help people work smarter

👩‍💻 Created by:
Gayatri Kanagaraj
Data Science student | Data Quality believer | Doing QA my way


---


