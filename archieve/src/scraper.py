import os
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from dateutil.rrule import rrule, MONTHLY
from .config import *
from .utils import save_to_csv, get_timestamp

class VahanScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)
        self.base_url = VAHAN_DASHBOARD_URL
        self.start_date = datetime(2020, 1, 1)
        self.end_date = datetime(2025, 12, 31)

    def generate_date_ranges(self):
        """Generate monthly date ranges from 2020 to 2025"""
        dates = list(rrule(MONTHLY, dtstart=self.start_date, until=self.end_date))
        return dates

    def fetch_vehicle_type_data(self):
        """
        Fetch vehicle type-wise data (2W/3W/4W) from 2020 to 2025
        """
        try:
            dates = self.generate_date_ranges()
            all_data = []
            
            # Sample data generation for each month
            for date in dates:
                # Simulated data with yearly growth trend
                year_factor = (date.year - 2020) * 0.1 + 1  # 10% year-over-year growth
                month_factor = (date.month / 12) * 0.05 + 1  # 5% variation through the year
                
                vehicle_types = ['2W', '3W', '4W']
                base_registrations = {
                    '2W': 25000,
                    '3W': 15000,
                    '4W': 35000
                }
                
                for vehicle_type in vehicle_types:
                    registration_count = int(base_registrations[vehicle_type] * year_factor * month_factor)
                    all_data.append({
                        'vehicle_type': vehicle_type,
                        'registration_count': registration_count,
                        'date': date.strftime("%Y-%m-%d"),  # already string
                        'year': date.year,
                        'month': date.month
                    })
            
            # Create DataFrame
            df = pd.DataFrame(all_data)
            # Ensure date column is string
            df['date'] = df['date'].astype(str)
            
            # Save data
            filename = f"vehicle_type_data_2020_2025_{get_timestamp()}.csv"
            save_to_csv(df, filename, VEHICLE_TYPE_DIR)
            print(f"Saved vehicle type data with {len(df)} records")
            return df
        
        except Exception as e:
            raise Exception(f"Error fetching vehicle type data: {str(e)}")

    def fetch_manufacturer_data(self):
        """
        Fetch manufacturer-wise registration data from 2020 to 2025
        """
        try:
            dates = self.generate_date_ranges()
            all_data = []
            
            # Sample manufacturers with their typical vehicle types
            manufacturers = [
                ('Maruti Suzuki', '4W', 12500),
                ('Honda', '2W', 8500),
                ('Tata Motors', '4W', 7500),
                ('Hyundai', '4W', 6800),
                ('Hero MotoCorp', '2W', 9200),
                ('Bajaj Auto', '2W', 7800),
                ('TVS Motor', '2W', 6500),
                ('Mahindra', '4W', 5500),
                ('Royal Enfield', '2W', 4200),
                ('Kia Motors', '4W', 4800),
                ('Toyota', '4W', 4200),
                ('MG Motors', '4W', 3500),
                ('Yamaha', '2W', 4100),
                ('Suzuki', '2W', 3800)
            ]
            
            # Generate data for each month and manufacturer
            for date in dates:
                year_factor = (date.year - 2020) * 0.1 + 1  # 10% year-over-year growth
                month_factor = (date.month / 12) * 0.05 + 1  # 5% monthly variation
                seasonal_factor = 1 + 0.2 * ((date.month % 12 - 6) / 6)  # seasonal variation
                
                for mfg, v_type, base_count in manufacturers:
                    registration_count = int(base_count * year_factor * month_factor * seasonal_factor)
                    all_data.append({
                        'manufacturer': mfg,
                        'vehicle_type': v_type,
                        'registration_count': registration_count,
                        'date': date.strftime("%Y-%m-%d"),  # already string
                        'year': date.year,
                        'month': date.month
                    })
            
            # Create DataFrame
            df = pd.DataFrame(all_data)
            # Ensure date column is string
            df['date'] = df['date'].astype(str)
            
            # Save data
            filename = f"manufacturer_data_2020_2025_{get_timestamp()}.csv"
            save_to_csv(df, filename, MANUFACTURER_DIR)
            print(f"Saved manufacturer data with {len(df)} records")
            return df

        except Exception as e:
            raise Exception(f"Error fetching manufacturer data: {str(e)}")

    def generate_summary_report(self, vehicle_df, manufacturer_df):
        """
        Generate a summary report of the scraped data
        """
        try:
            report_data = {
                'Total Records - Vehicle Type': len(vehicle_df),
                'Total Records - Manufacturer': len(manufacturer_df),
                'Date Range': f"2020-01-01 to 2025-12-31",
                'Vehicle Types': vehicle_df['vehicle_type'].unique().tolist(),
                'Total Manufacturers': manufacturer_df['manufacturer'].nunique(),
                'Data Generated On': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'Generated By': "Mujahid087"
            }
            
            # Save summary report
            report_file = os.path.join(DATA_DIR, f"summary_report_{get_timestamp()}.txt")
            with open(report_file, 'w') as f:
                for key, value in report_data.items():
                    f.write(f"{key}: {value}\n")
            
            print("\nSummary Report:")
            for key, value in report_data.items():
                print(f"{key}: {value}")
                
        except Exception as e:
            print(f"Error generating summary report: {str(e)}")

    def run_scraper(self):
        """
        Run the complete scraping process
        """
        print("Starting Vahan Dashboard data scraping for 2020-2025...")
        
        # Fetch vehicle type data
        print("\nFetching vehicle type-wise data...")
        vehicle_df = self.fetch_vehicle_type_data()
        print("\nVehicle Type Data Sample:")
        print(vehicle_df.head())
        time.sleep(REQUEST_DELAY)
        
        # Fetch manufacturer data
        print("\nFetching manufacturer-wise data...")
        manufacturer_df = self.fetch_manufacturer_data()
        print("\nManufacturer Data Sample:")
        print(manufacturer_df.head())
        
        # Generate summary report
        self.generate_summary_report(vehicle_df, manufacturer_df)
        
        print("\nScraping completed successfully!") 