import requests

class IPMAService:
    base_url = "https://api.ipma.pt/open-data/"

    def __init__(self):
        self.session = requests.Session()

    def _request(self, endpoint):
        default_url = f"{self.base_url}{endpoint}"
        try:
            response = self.session.get(default_url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"Error HTTP {response.status_code}: {e}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Connection errorr: {e}")
            return None

    #Public function to return all districts for Portugal and other information
    def get_district(self):
        #api https://api.ipma.pt/open-data/distrits-islands.json
        endpoint = "distrits-islands.json"
        data = self._request(endpoint)

        if data and 'data' in data:
            return data['data']
        return None

    #Public function to return Weather Forecast daily up to 5 days for specific location
    def get_forecast_by_id(self, globalIdLocal):
        endpoint = f"forecast/meteorology/cities/daily/{globalIdLocal}.json"
        return self._request(endpoint)

    #Public function to return Weather Forecast daily up to 5 days aggregate for all local
    def get_five_days_forecast_by_City(self):
        #https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{globalIdLocal}.json
        district = self.get_district()
        if not district:
            print("The list of districts could not be obtained.")
            return None

        all_data = []

        for dist in district:
            data = self.get_forecast_by_id(dist['globalIdLocal'])
            if data is not None and 'data' in data:
                dist_name = dist['local']
                for forecast in data['data']:
                    forecast['district'] = dist_name
                    #Append each forecast to the list (all_data)
                    all_data.append(forecast)
        return all_data


ipma_service = IPMAService()
#district = ipma_district.get_district()
#for d in district:
#    print(f"{d['local']}")

#forecast = ipma_service.get_five_days_forecast_by_City()
#if forecast:
#    print(forecast)

forecas_by_city = ipma_service.get_forecast_by_id(1050200)
print(forecas_by_city)