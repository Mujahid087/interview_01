# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import os

# st.set_page_config(page_title="Vehicle Registration Growth Dashboard", layout="wide")

# # ---- Sidebar ----
# st.sidebar.title("Filters")
# st.sidebar.markdown("Select filters to customize the dashboard.")

# # ---- Data Loading ----
# @st.cache_data
# def load_data():
#     vehicle_metrics = pd.read_csv("data/metrics/vehicle_type_yoy_qoq_metrics.csv", parse_dates=["year_month"])
#     return vehicle_metrics

# vehicle_metrics = load_data()

# # Ensure 'year_month' is datetime and create a date column for filtering
# vehicle_metrics["year_month"] = pd.to_datetime(vehicle_metrics["year_month"])
# vehicle_metrics["year_month_date"] = vehicle_metrics["year_month"].dt.date

# # ---- Date Range Selection ----
# all_dates = vehicle_metrics["year_month_date"].drop_duplicates().sort_values()
# min_date = all_dates.min()
# max_date = all_dates.max()
# date_range = st.sidebar.slider(
#     "Select Date Range",
#     min_value=min_date,
#     max_value=max_date,
#     value=(min_date, max_date),
#     format="YYYY-MM"
# )

# # ---- Category Filter ----
# vehicle_types = vehicle_metrics["vehicle_type"].unique()
# selected_categories = st.sidebar.multiselect(
#     "Vehicle Categories", options=vehicle_types, default=list(vehicle_types)
# )

# # ---- Data Filtering ----
# vehicle_filtered = vehicle_metrics[
#     (vehicle_metrics["year_month_date"] >= date_range[0]) &
#     (vehicle_metrics["year_month_date"] <= date_range[1]) &
#     (vehicle_metrics["vehicle_type"].isin(selected_categories))
# ]

# # ---- Main Layout ----
# st.title("Vehicle Registration Growth Dashboard")
# st.markdown(
#     """
#     This dashboard displays **Year-over-Year (YoY)** and **Quarter-over-Quarter (QoQ)** growth trends 
#     for vehicle registrations by category. Use the sidebar to filter data.
#     """
# )

# # ---- User Selection for Growth Metric ----
# growth_metric = st.radio(
#     "Select Growth Metric to Display:",
#     options=["YoY Growth (%)", "QoQ Growth (%)"],
#     index=0,
#     horizontal=True,
#     key="growth_metric_radio"
# )

# metric_column = "YoY_Growth_%" if growth_metric == "YoY Growth (%)" else "QoQ_Growth_%"

# st.subheader(f"{growth_metric} by Vehicle Category")
# fig_cat = px.line(
#     vehicle_filtered,
#     x="year_month", y=metric_column,
#     color="vehicle_type",
#     markers=True,
#     labels={metric_column: "Growth (%)", "year_month": "Month"},
#     title=f"{growth_metric} by Vehicle Type"
# )
# st.plotly_chart(fig_cat, use_container_width=True)

# # ---- Show Data ----
# with st.expander("Show Raw Data"):
#     st.write("Vehicle Type Metrics Data", vehicle_filtered) 



import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Vehicle Registration Growth Dashboard", layout="wide")

# ---- Sidebar ----
st.sidebar.title("Filters")
st.sidebar.markdown("Select filters to customize the dashboard.")

# ---- Data Loading ----
@st.cache_data
def load_data():
    vehicle_metrics = pd.read_csv("data/metrics/vehicle_type_yoy_qoq_metrics.csv", parse_dates=["year_month"])
    manufacturer_metrics = pd.read_csv("data/metrics/manufacturer_yoy_qoq_metrics.csv", parse_dates=["year_month"])
    return vehicle_metrics, manufacturer_metrics

vehicle_metrics, manufacturer_metrics = load_data()

# Ensure 'year_month' is datetime and create a date column for filtering
vehicle_metrics["year_month"] = pd.to_datetime(vehicle_metrics["year_month"])
vehicle_metrics["year_month_date"] = vehicle_metrics["year_month"].dt.date

manufacturer_metrics["year_month"] = pd.to_datetime(manufacturer_metrics["year_month"])
manufacturer_metrics["year_month_date"] = manufacturer_metrics["year_month"].dt.date

# ---- Date Range Selection ----
all_dates = pd.concat([
    vehicle_metrics["year_month_date"], 
    manufacturer_metrics["year_month_date"]
]).drop_duplicates().sort_values()
min_date = all_dates.min()
max_date = all_dates.max()
date_range = st.sidebar.slider(
    "Select Date Range",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date),
    format="YYYY-MM"
)

# ---- Category & Manufacturer Filters ----
vehicle_types = vehicle_metrics["vehicle_type"].unique()
selected_categories = st.sidebar.multiselect(
    "Vehicle Categories", options=vehicle_types, default=list(vehicle_types)
)

manufacturers = manufacturer_metrics["vehicle_type"].unique()
selected_manufacturers = st.sidebar.multiselect(
    "Manufacturer (Vehicle Type)", options=manufacturers, default=list(manufacturers)
)

# ---- Data Filtering ----
vehicle_filtered = vehicle_metrics[
    (vehicle_metrics["year_month_date"] >= date_range[0]) &
    (vehicle_metrics["year_month_date"] <= date_range[1]) &
    (vehicle_metrics["vehicle_type"].isin(selected_categories))
]

manufacturer_filtered = manufacturer_metrics[
    (manufacturer_metrics["year_month_date"] >= date_range[0]) &
    (manufacturer_metrics["year_month_date"] <= date_range[1]) &
    (manufacturer_metrics["vehicle_type"].isin(selected_manufacturers))
]

# ---- Main Layout ----
st.title("Vehicle Registration Growth Dashboard")
st.markdown(
    """
    This dashboard displays **Year-over-Year (YoY)** and **Quarter-over-Quarter (QoQ)** growth trends 
    for vehicle registrations by category and manufacturer. Use the sidebar to filter data.
    """
)

# ---- User Selection for Growth Metric ----
growth_metric = st.radio(
    "Select Growth Metric to Display:",
    options=["YoY Growth (%)", "QoQ Growth (%)"],
    index=0,
    horizontal=True,
    key="growth_metric_radio"
)

metric_column = "YoY_Growth_%" if growth_metric == "YoY Growth (%)" else "QoQ_Growth_%"

col1, col2 = st.columns(2)

with col1:
    st.subheader(f"{growth_metric} by Vehicle Category")
    fig_cat = px.line(
        vehicle_filtered,
        x="year_month", y=metric_column,
        color="vehicle_type",
        markers=True,
        labels={metric_column: "Growth (%)", "year_month": "Month"},
        title=f"{growth_metric} by Vehicle Type"
    )
    st.plotly_chart(fig_cat, use_container_width=True)

with col2:
    st.subheader(f"{growth_metric} by Manufacturer Vehicle Type")
    fig_man = px.line(
        manufacturer_filtered,
        x="year_month", y=metric_column,
        color="vehicle_type",
        markers=True,
        labels={metric_column: "Growth (%)", "year_month": "Month"},
        title=f"{growth_metric} by Manufacturer Vehicle Type"
    )
    st.plotly_chart(fig_man, use_container_width=True)

# ---- Show Data ----
with st.expander("Show Raw Data"):
    st.write("Vehicle Type Metrics Data", vehicle_filtered)
    st.write("Manufacturer Metrics Data", manufacturer_filtered)