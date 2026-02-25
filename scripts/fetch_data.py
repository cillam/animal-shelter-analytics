import httpx
from pathlib import Path
from datetime import datetime

DATA_DIR = Path(__file__).parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)

URL = "https://data.sonomacounty.ca.gov/api/views/924a-vesw/rows.csv?accessType=DOWNLOAD"

def fetch_shelter_data():
    print(f"Fetching data from Sonoma County...")
    response = httpx.get(URL, follow_redirects=True)
    response.raise_for_status()
    
    output_path = DATA_DIR / "animal_shelter_data.csv"
    output_path.write_bytes(response.content)
    
    print(f"Saved to {output_path}")
    print(f"Downloaded at: {datetime.now().isoformat()}")
    print(f"Size: {len(response.content) / 1024:.1f} KB")

if __name__ == "__main__":
    fetch_shelter_data()
