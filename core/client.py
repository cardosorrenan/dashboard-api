import os, json, requests


class Client():
    URL_DATASERVICE = os.environ.get('URL_DATASERVICE')
    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    
    def get(self, endpoint, params):
        url = self.URL_DATASERVICE + endpoint
        response = requests.get(url, params=params)
        data = response.json()
        return { 'result': data }


class ClientMock():
    
    def get(self, path):
        data = []
        try:
            with open(path, 'r') as f:
                data = json.load(f)
        except Exception as e:
            print(e)
        return data