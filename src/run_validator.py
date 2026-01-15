import pandas as pd
import os
import json
from validator import DataValidator

data_folder = "data/"
report_folder = "reports/"

# Create reports folder if not exists
os.makedirs(report_folder, exist_ok=True)

summary = []

all_errors = {}

for file in os.listdir(data_folder):
    if file.endswith(".csv"):
        print(f"\n🔍 Checking: {file}")

        file_path = os.path.join(data_folder, file)
        df = pd.read_csv(file_path)
        validator = DataValidator(df)
        errors = validator.run_all_checks()

        if errors:
            print(f"⚠ Issues found in {file}:")
            print(errors)
            status = "Failed"
        else:
            print(f"✅ {file} PASSED all checks!")
            status = "Passed"

        print("-" * 50)

        # Save to master error dictionary
        all_errors[file] = errors

        # Add summary row
        summary.append({"File": file, "Status": status, "ErrorCount": len(errors)})

# Save summary CSV
summary_df = pd.DataFrame(summary)
summary_df.to_csv(os.path.join(report_folder, "summary.csv"), index=False)

# Save JSON report
with open(os.path.join(report_folder, "error_report.json"), "w") as f:
    json.dump(all_errors, f, indent=4)

print("\n📁 Reports saved in 'reports/'")
