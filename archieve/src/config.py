VAHAN_DASHBOARD_URL = "https://vahan.parivahan.gov.in/vahan4dashboard/"

# Data directory paths
DATA_DIR = "data"
VEHICLE_TYPE_DIR = "data/vehicle_type"
MANUFACTURER_DIR = "data/manufacturer"

# Request headers to mimic browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}

# Time delay between requests (in seconds)
REQUEST_DELAY = 2

# CSV Settings
CSV_ENCODING = 'utf-8'