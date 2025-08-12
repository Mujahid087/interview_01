import pandas as pd
import os

def calculate_yoy_qoq(df, date_col, group_cols, value_col):
    # Ensure date column is datetime
    df[date_col] = pd.to_datetime(df[date_col], format='%Y-%m')
    df = df.sort_values(date_col)

    # Aggregate if needed
    agg_df = df.groupby(group_cols + [date_col])[value_col].sum().reset_index()

    # Pivot for easier calculation
    piv = agg_df.pivot_table(index=group_cols, columns=date_col, values=value_col)

    # Calculate YoY and QoQ growth
    yoy_growth = piv.pct_change(periods=12, axis=1) * 100  # 12 months prior
    qoq_growth = piv.pct_change(periods=3, axis=1) * 100   # 3 months prior

    # Melt back to long format for saving
    yoy_melt = yoy_growth.reset_index().melt(id_vars=group_cols, var_name=date_col, value_name='YoY_Growth_%')
    qoq_melt = qoq_growth.reset_index().melt(id_vars=group_cols, var_name=date_col, value_name='QoQ_Growth_%')

    # Merge growth metrics
    metrics = pd.merge(yoy_melt, qoq_melt, on=group_cols + [date_col])
    return metrics

# Load your manufacturer data
df_manufacturer = pd.read_csv('data/processed/manufacturer_monthly_aggregated_processed.csv')

# If you don't have a 'manufacturer' column, but want to group by vehicle_type:
metrics_manufacturer = calculate_yoy_qoq(
    df_manufacturer,
    date_col='year_month',
    group_cols=['vehicle_type'],
    value_col='registration_count'
)

# Create metrics directory if it doesn't exist
os.makedirs('data/metrics', exist_ok=True)

# Save to CSV
metrics_manufacturer.to_csv('data/metrics/manufacturer_yoy_qoq_metrics.csv', index=False)