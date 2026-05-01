import time
import hmac
import hashlib
import requests
from urllib.parse import urlencode
import logging

logger = logging.getLogger(__name__)

class BinanceFuturesClient:
    BASE_URL = "https://testnet.binancefuture.com"

    def __init__(self, api_key: str, api_secret: str):
        self.api_key = api_key
        self.api_secret = api_secret
        self.session = requests.Session()
        self.session.headers.update({
            "X-MBX-APIKEY": self.api_key
        })

    def _generate_signature(self, query_string: str) -> str:
        return hmac.new(
            self.api_secret.encode("utf-8"),
            query_string.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()

    def send_signed_request(self, method: str, endpoint: str, params: dict = None):
        if params is None:
            params = {}
        
        # Binance requires a timestamp for signed requests
        params["timestamp"] = int(time.time() * 1000)
        query_string = urlencode(params, doseq=True)
        signature = self._generate_signature(query_string)
        
        url = f"{self.BASE_URL}{endpoint}?{query_string}&signature={signature}"
        
        logger.info(f"Sending {method} request to {endpoint}")
        
        try:
            response = self.session.request(method, url)
            response.raise_for_status()
            data = response.json()
            logger.info(f"API Response: {data}")
            return data
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP Error: {e.response.text}")
            raise Exception(f"API Error: {e.response.json().get('msg', 'Unknown Error')}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Network Error: {e}")
            raise Exception(f"Network Error: {e}")
          
