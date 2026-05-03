from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .services.route_service import get_route
from .services.optimizer import calculate_fuel_stops


@api_view(['POST'])
def route_api(request):
    start = request.data.get("start")
    end = request.data.get("end")

    if not start or not end:
        return Response({"error": "start and end required"}, status=400)

    route = get_route(start, end)
    fuel_plan = calculate_fuel_stops(route["distance_miles"])

    return Response({
        "distance_miles": route["distance_miles"],
        "fuel_plan": fuel_plan
    })