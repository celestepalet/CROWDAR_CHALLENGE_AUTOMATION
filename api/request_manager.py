from api.constants import BASE_URL, AUTHENTICATION
import requests


class RequestManager:
    """This class provide support for API requests"""

    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url

    def make_request(self, request_method, endpoint, authentication=AUTHENTICATION, data=None):
        """Sends request to api and return status code and response"""
        url = f"{self.base_url}{endpoint}"
        response = requests.request(request_method, url, json=data, auth=authentication)
        return response.status_code, response
