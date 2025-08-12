import os
import json
import pandas as pd
import numpy as np
from datetime import datetime
from pathlib import Path

def create_directories():
    """Create necessary directories for storing data"""
    directories = ['data', 'data/vehicle_type', 'data/manufacturer', 'data/analysis']
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)

def save_to_csv(df, filename, directory):
    """Save DataFrame to CSV file with additional analysis"""
    # Ensure directory exists
    os.makedirs(directory, exist_ok=True)
    
    # Create full filepath
    filepath = os.path.join(directory, filename)
    
    # Add some basic statistics
    df['year_month'] = pd.to_datetime(df['date']).dt.to_period('M')
    
    # Save main DataFrame to CSV
    df.to_csv(filepath, index=False)
    print(f"\nData saved to {filepath}")
    
    # Generate and save monthly aggregates
    monthly_agg = df.groupby(['year_month', 'vehicle_type'])['registration_count'].sum().reset_index()
    monthly_filepath = os.path.join(directory, f"monthly_agg_{filename}")
    monthly_agg.to_csv(monthly_filepath, index=False)
    
    # Print summary statistics
    print("\nSummary Statistics:")
    print(f"Total records: {len(df)}")
    print(f"Date range: {df['date'].min()} to {df['date'].max()}")
    print(f"Total registration count: {df['registration_count'].sum():,}")
    
    if 'manufacturer' in df.columns:
        print(f"Number of manufacturers: {df['manufacturer'].nunique()}")
    
    print("\nMonthly aggregate data saved to:", monthly_filepath)

def get_timestamp():
    """Get current timestamp in YYYY-MM-DD_HHMMSS format"""
    return datetime.now().strftime("%Y-%m-%d_%H%M%S")

def handle_error(error, message):
    """Handle and log errors"""
    error_time = datetime.now().strftime("%Y-%m-% d %H:%M:%S")
    error_msg = f"[{error_time}] Error: {message}\nDetails: {str(error)}"
    print(error_msg)
    
    # Log error to file
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    with open(os.path.join(log_dir, "error_log.txt"), "a") as f:
        f.write(error_msg + "\n\n") 


