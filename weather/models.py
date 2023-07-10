from django.db import models


class WeatherData(models.Model):
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    detailing_type = models.CharField(max_length=20)
    forecast_data = models.JSONField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Weather data for {self.lat}, {self.lon} is {self.forecast_data}"
