import requests

class WeatherWarner:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_temperature(self, city):
        """Holt die Temperatur von einer externen API."""
        response = requests.get(f"{self.api_url}/v1/current?city={city}")
        if response.status_code == 200:
            data = response.json()
            return data.get("temperature", 0.0)
        return None

    def check_and_warn(self, city, threshold=35.0):
        """Prüft die Temperatur und gibt eine Warnung aus."""
        temp = self.fetch_temperature(city)
        if temp is None:
            return "Fehler: Wetterdaten nicht verfügbar"
        
        if temp >= threshold:
            return f"WARNUNG: Hitzealarm in {city}! Es sind {temp}°C."
        
        return f"Alles im grünen Bereich in {city}."