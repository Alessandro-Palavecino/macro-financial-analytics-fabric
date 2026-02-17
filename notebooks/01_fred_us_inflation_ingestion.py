"""
Notebook: 01_fred_us_inflation_ingestion
Author: Alessandro Palavecino
Project: Macroeconomic Financial Analytics Platform
Description: Ingest US CPI (Inflation) data from FRED API.
"""

import requests
import json
from datetime import datetime

# -----------------------------
# Configuration
# -----------------------------

API_KEY = "YOUR_FRED_API_KEY"  # Replace in Fabric using secure storage
SERIES_ID = "CPIAUCSL"  # US Consumer Price Index
BASE_URL = "https://api.stlouisfed.org/fred/series/observations"

# -----------------------------
# API Request
# -----------------------------

params = {
    "series_id": SERIES_ID,
    "api_key": API_KEY,
    "file_type": "json"
}

response = requests.get(BASE_URL, params=params)

if response.status_code != 200:
    raise Exception(f"API request failed with status {response.status_code}")

data = response.json()

# -----------------------------
# Basic Validation
# -----------------------------

if "observations" not in data:
    raise Exception("Invalid API response structure")

observations = data["observations"]

print(f"Total records retrieved: {len(observations)}")

# -----------------------------
# Transform Preview
# -----------------------------

preview = [
    {
        "date": obs["date"],
        "value": obs["value"],
        "ingestion_timestamp": datetime.utcnow().isoformat()
    }
    for obs in observations[:5]
]

print("Sample preview:")
print(json.dumps(preview, indent=2))
