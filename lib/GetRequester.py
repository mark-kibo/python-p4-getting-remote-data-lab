import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.content
        else:
            return "invalid"

    def load_json(self):
        my_data=self.get_response_body()
        return json.loads(my_data)