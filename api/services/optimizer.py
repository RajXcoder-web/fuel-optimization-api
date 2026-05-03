import pandas as pd
import os

# Load CSV once
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CSV_PATH = os.path.join(BASE_DIR, "services", "fuel-prices-for-be-assessment.csv")

fuel_data = pd.read_csv(CSV_PATH)


def calculate_fuel_stops(distance_miles):
    if distance_miles <= 0:
        return []

    # Sort cheapest stations
    sorted_stations = fuel_data.sort_values(by="Retail Price")

    stops = []
    remaining_distance = distance_miles

    # simple logic (demo)
    for _, row in sorted_stations.iterrows():
        if remaining_distance <= 0:
            break

        stops.append({
            "station": row["Truckstop Name"],
            "price": row["Retail Price"]
        })

        remaining_distance -= 100  # assume 100 miles per stop

    return stops