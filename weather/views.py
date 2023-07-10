from datetime import datetime, timedelta

import requests
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import WeatherData


@csrf_exempt
def weather_api(request):
    if request.method == "POST":
        lat = request.POST.get("lat").strip()
        lon = request.POST.get("lon").strip()
        detailing_type = request.POST.get("detailing_type")

        weather_data = WeatherData.objects.filter(
            lat=lat, lon=lon, detailing_type=detailing_type
        ).first()

        if weather_data:
            time_difference = datetime.now() - weather_data.last_updated.replace(
                tzinfo=None
            )
            if time_difference < timedelta(minutes=settings.DATA_EXPIRY_MINUTES):
                forecast_data = weather_data.forecast_data

                return render(
                    request,
                    "weather/weather_forecast.html",
                    {"forecast_data": forecast_data},
                )

        exclude_params = ""
        if detailing_type == "minute":
            exclude_params = "current,hourly,daily,alerts"
        elif detailing_type == "hourly":
            exclude_params = "current,minutely,daily,alerts"
        elif detailing_type == "daily":
            exclude_params = "current,minutely,hourly,alerts"
        else:
            return JsonResponse({"error": "Invalid detailing type"}, status=400)

        url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&exclude={exclude_params}&appid={settings.OPENWEATHERMAP_API_KEY}"

        response = requests.get(url)

        if response.status_code == 200:
            forecast_data = response.json()
            keys = ['cod', 'message', 'cnt']

            for key in keys:
                forecast_data.pop(key, None)

            if not weather_data:
                weather_data = WeatherData(
                    lat=lat,
                    lon=lon,
                    detailing_type=detailing_type,
                    forecast_data=forecast_data,
                )
            weather_data.save()
       
        return render(
            request,
            "weather/weather_forecast.html",
            {"forecast_data": forecast_data},
        )

    return render(request, "weather/index.html")
