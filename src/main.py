from datetime import datetime
from .config import CITIES
from .weather_client import get_weather_for_city
from .storage_s3 import upload_weather_data

def collect_weather_data():
    all_data = []
    timestamp = datetime.utcnow().isoformat()

    for city in CITIES:
        weather = get_weather_for_city(city)
        if weather:
            weather["timestamp"] = timestamp
            all_data.append(weather)

    return all_data

def main():
    print("[INFO] Starting weather data collection...")
    print(f"[INFO] Tracking cities: {', '.join(CITIES)}")

    data = collect_weather_data()

    if not data:
        print("[WARN] No data collected. Nothing to upload.")
        return

    print("[INFO] Collected data:")
    for entry in data:
        print(
            f"  {entry['city']}: {entry['temperature']}°, "
            f"{entry['humidity']}% humidity, {entry['conditions']}"
        )

    upload_weather_data(data)
    print("[INFO] Done.")

if __name__ == "__main__":
    main()

