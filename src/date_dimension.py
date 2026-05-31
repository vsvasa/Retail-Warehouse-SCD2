from datetime import datetime
import pandas as pd

def generate_date_dimension(start_date = '2024-01-01', end_date = '2030-12-31'):
    dates = pd.date_range(start = start_date, end = end_date, freq = 'D')
    date_df = pd.DataFrame({
        'date_key': dates.to_series().apply(lambda x: int(x.strftime('%Y%m%d'))),
        'full_date': dates,
        'day_name': dates.day_name(),
        'month_name': dates.month_name(),
        'month': dates.month,
        'quarter': dates.quarter,
        'year': dates.year
    })
    return date_df

