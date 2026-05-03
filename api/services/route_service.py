import requests
from django.conf import settings


def get_route(start, end):
    url = "https://api.openrouteservice.org/v2/directions/driving-car"

    headers = {
        "Authorization": settings.ORS_API_KEY,
        "Content-Type": "application/json"
    }

    body = {
        "coordinates": [
            [-74.0060, 40.7128],  # TEMP (NY)
            [-118.2437, 34.0522]  # TEMP (LA)
        ]
    }

    response = requests.post(url, json=body, headers=headers)
    data = response.json()

    distance_meters = data["routes"][0]["summary"]["distance"]
    distance_miles = distance_meters * 0.000621371

    return {
        "distance_miles": distance_miles
    }