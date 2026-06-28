import unittest
from unittest.mock import patch, MagicMock
from weather_service import WeatherWarner

class TestWeatherWarner(unittest.TestCase):

    @patch('weather_service.requests.get')
    def test_check_and_warn_heat_trigger(self, mock_get):
        """Testet, ob der Alarm bei Hitze korrekt ausgelöst wird."""
        # Vorbereitung des Mocks: Wir simulieren eine erfolgreiche API-Antwort (200) mit 36 Grad
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"temperature": 36.0}
        mock_get.return_value = mock_response

        warner = WeatherWarner("http://fake-api.com")
        
        # Ausführung
        result = warner.check_and_warn("Berlin", threshold=35.0)
        
        # Behauptung (Assertion)
        self.assertEqual(result, "WARNUNG: Hitzealarm in Berlin! Es sind 36.0°C.")
        # Überprüfen, ob die API auch mit den richtigen Parametern aufgerufen wurde
        mock_get.assert_called_once_with("http://fake-api.com/v1/current?city=Berlin")

if __name__ == '__main__':
    unittest.main()