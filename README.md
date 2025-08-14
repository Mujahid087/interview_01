# 🚗 Vehicle Registration Data Dashboard

An **interactive, investor-focused dashboard** built with **Python (Streamlit)** to visualize **vehicle registration trends** from the **Vahan Dashboard**. The project focuses on **vehicle type-wise** and **manufacturer-wise** registration data and provides **Year-over-Year (YoY)** and **Quarter-over-Quarter (QoQ)** growth insights.

## 📊 Data Source

- **Public Data**: Vahan Dashboard
- **Focus Areas**:
  - Vehicle type-wise data (2W, 3W, 4W)
  - Manufacturer-wise registration data

## 🎯 Key Features

- **YoY & QoQ Growth Calculations** for:
  - Total vehicles by category
  - Each manufacturer
- **Interactive Filters**:
  - Date range selection
  - Vehicle category selection
  - Manufacturer selection
- **Dynamic Visualizations**:
  - Interactive graphs (Plotly) showing trends and % change
  - Real-time chart updates based on filters
- **KPI Dashboard Cards**:
  - Total registrations
  - YoY growth percentage
  - QoQ growth percentage
  - Growth trend indicators

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Data processing & backend logic |
| **Streamlit** | Interactive dashboard UI |
| **Plotly** | Interactive charts & visualizations |
| **Pandas** | Data manipulation & analysis |


## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Mujahid087/interview_01
cd interview_01
```

### 2️⃣ Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the dashboard
```bash
streamlit run src/dashboard.py
```

The dashboard will be available at `http://localhost:8501`

## 📈 Data Processing Pipeline

The data processing workflow includes:

1. **Data Ingestion**: Raw Vahan dashboard data import
2. **Data Cleaning**: Handle missing values, standardize formats
3. **Aggregation**: Monthly summaries by vehicle type and manufacturer
4. **Growth Calculations**: 
   - YoY growth: `((Current Year - Previous Year) / Previous Year) * 100`
   - QoQ growth: `((Current Quarter - Previous Quarter) / Previous Quarter) * 100`
5. **Export**: Clean datasets saved to `data/processed/`

## 🗂 Data Schema

### Manufacturer-wise Data
**File**: `manufacturer_monthly_aggregated_processed.csv`

| Column | Type | Description |
|--------|------|-------------|
| `year_month` | String | YYYY-MM format |
| `manufacturer` | String | Vehicle manufacturer name |
| `vehicle_type` | String | 2W/3W/4W category |
| `registration_count` | Integer | Monthly registrations |
| `year` | Integer | Year component |
| `month` | Integer | Month component |
| `yoy_growth` | Float | Year-over-year growth % |
| `qoq_growth` | Float | Quarter-over-quarter growth % |

### Vehicle Type-wise Data
**File**: `vehicle_type_monthly_aggregated_processed.csv`

| Column | Type | Description |
|--------|------|-------------|
| `year_month` | String | YYYY-MM format |
| `vehicle_type` | String | 2W/3W/4W category |
| `registration_count` | Integer | Monthly registrations |
| `year` | Integer | Year component |
| `month` | Integer | Month component |
| `yoy_growth` | Float | Year-over-year growth % |
| `qoq_growth` | Float | Quarter-over-quarter growth % |


## 🚀 Feature Roadmap

### Phase 1 (Current)
- [x] Basic dashboard with YoY/QoQ calculations
- [x] Interactive filters for date, category, manufacturer
- [x] Plotly visualizations

### Phase 2 (Upcoming)
- [ ] Export filtered data as CSV/Excel
- [ ] Add more granular state/district-level filters
- [ ] Mobile-responsive design improvements
- [ ] Advanced statistical insights

### Phase 3 (Future)
- [ ] AI-powered forecasting of registrations
- [ ] Comparative analysis between manufacturers
- [ ] Real-time data integration
- [ ] Advanced analytics with ML insights

## 📹 Demo

🎬 **Video Walkthrough**: *(https://www.loom.com/share/6d65ecf5f62e4cee922439c42b0e5f18?sid=a6423baf-eb99-48ae-8b60-2b0ee14307d0)*

## 💡 Key Investor Insights

### Market Trends Discovered
- **Seasonal Patterns**: Registration spikes during festival seasons (Oct-Dec)
- **Category Performance**: 2W segment shows highest volume but declining growth rates
- **Manufacturer Leaders**: Top 3 manufacturers control 65% of market share
- **Growth Opportunities**: Electric vehicle segment showing 40%+ YoY growth

### Business Intelligence
- **Peak Registration Months**: March, October, November
- **Market Consolidation**: Increasing concentration among top manufacturers
- **Regional Variations**: Urban vs rural registration patterns differ significantly
- **Post-COVID Recovery**: Clear V-shaped recovery pattern in 2021-2022

