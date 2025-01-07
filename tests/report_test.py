import numpy as np
import os
import pandas as pd
import quantstats as qs


# Sample data generation for the example
def generate_sample_data() -> pd.Series:
    np.random.seed()
    dates = pd.date_range(start="2023-01-01", end="2023-12-31")
    returns = np.random.normal(0.001, 0.02, len(dates))
    return pd.Series(data=returns, index=dates)

sample_data = generate_sample_data()
sample_benchmark = generate_sample_data()
stock = qs.utils.download_returns("META")
qs.reports.html(
    returns=sample_data,
    benchmark=sample_benchmark,
    output=os.path.join("test_output", "report_test.html"),
    compounded=True,
    benchmark_title="SPX"
)
