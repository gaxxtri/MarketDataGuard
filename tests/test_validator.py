import pandas as pd
from src.validator import DataValidator


def test_missing_values():
    df = pd.DataFrame({"Date":["2024-01-01"], "Open":[100], "High":[110], "Low":[90], "Close":[105], "Volume":[None]})
    v = DataValidator(df)
    v.check_missing_values()
    assert "missing_values" in v.errors

def test_negative_price():
    df = pd.DataFrame({"Date":["2024-01-01"], "Open":[-10], "High":[10], "Low":[5], "Close":[9], "Volume":[2000]})
    v = DataValidator(df)
    v.check_price_non_negative()
    assert "non_positive_prices" in v.errors
