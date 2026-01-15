import pandas as pd
import numpy as np

class DataValidator:
    def __init__(self, df):
        self.df = df
        self.errors = {}

    def log(self, rule_name, message):
        if rule_name not in self.errors:
            self.errors[rule_name] = []
        self.errors[rule_name].append(message)

    def check_required_columns(self, required_cols):
        missing_cols = [c for c in required_cols if c not in self.df.columns]
        if missing_cols:
            self.log("missing_columns", f"Missing columns: {missing_cols}")
            return False
        return True

    def check_missing_values(self):
        missing = self.df.isnull().sum()
        missing_dict = missing[missing > 0].to_dict()

        if missing_dict:
            self.log("missing_values", missing_dict)
            return False
        return True

    def check_price_non_negative(self):
        price_cols = ["Open", "High", "Low", "Close"]
        for col in price_cols:
            invalid_rows = self.df[self.df[col] <= 0]
            if not invalid_rows.empty:
                self.log("non_positive_prices", f"{col} has non-positive values at indexes {invalid_rows.index.tolist()}")
                return False
        return True

    def check_volume_non_negative(self):
        invalid_rows = self.df[self.df["Volume"] < 0]
        if not invalid_rows.empty:
            self.log("negative_volume", f"Negative volume at indexes {invalid_rows.index.tolist()}")
            return False
        return True

    def check_price_bounds(self):
        invalid = self.df[
            (self.df["High"] < self.df["Open"]) |
            (self.df["High"] < self.df["Close"]) |
            (self.df["Low"] > self.df["Open"]) |
            (self.df["Low"] > self.df["Close"])
        ]
        if not invalid.empty:
            self.log("price_bound_violation", f"Invalid price bounds at indexes {invalid.index.tolist()}")
            return False
        return True

    def check_date_format_and_order(self):
        try:
            self.df["Date"] = pd.to_datetime(self.df["Date"], errors="raise")
        except Exception:
            self.log("invalid_date_format", "Some Date values are not valid datetime format")
            return False

        if not self.df["Date"].is_monotonic_increasing:
            self.log("unsorted_dates", "Dates are not in ascending order")
            return False

        return True

    def check_duplicates(self):
        duplicates = self.df[self.df.duplicated()]
        if not duplicates.empty:
            self.log("duplicate_rows", f"Duplicate rows at indexes {duplicates.index.tolist()}")
            return False
        return True

    def run_all_checks(self):
        required = ["Date", "Open", "High", "Low", "Close", "Volume"]

        self.check_required_columns(required)
        self.check_missing_values()
        self.check_price_non_negative()
        self.check_volume_non_negative()
        self.check_price_bounds()
        self.check_date_format_and_order()
        self.check_duplicates()

        return self.errors
