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
            print(f"Erro HTTP {response.status_code}: {e}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Erro de Conexão: {e}")
            return None

    #Public function to return all districts for Portugal and other information
    def get_district(self):
        #api https://api.ipma.pt/open-data/distrits-islands.json
        endpoint = "distrits-islands.json"
        data = self._request(endpoint)

        if data and 'data' in data:
            for d in data['data']:
                print(f"{d['local']}")
        return None

ipma_district = IPMAService()
district = ipma_district.get_district()