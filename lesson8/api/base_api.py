import requests
from typing import Dict, Any, Optional
from requests.exceptions import RequestException


class BaseAPI:
    """Базовый класс для работы с API."""
    
    def __init__(self, base_url: str, headers: Optional[Dict[str, str]] = None):
        self.base_url = base_url.rstrip('/')
        self.headers = headers or {}
        self.session = requests.Session()
        self.session.headers.update(self.headers)
    
    def _request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """Выполняет HTTP запрос."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            return response
        except RequestException as e:
            error_msg = f"Ошибка при выполнении запроса {method} {url}: {str(e)}"
            if hasattr(e, 'response') and e.response is not None:
                error_msg += f"\nСтатус: {e.response.status_code}"
                try:
                    error_msg += f"\nОтвет: {e.response.text}"
                except:
                    pass
            raise Exception(error_msg)
    
    def post(self, endpoint: str, **kwargs) -> requests.Response:
        return self._request('POST', endpoint, **kwargs)
    
    def get(self, endpoint: str, **kwargs) -> requests.Response:
        return self._request('GET', endpoint, **kwargs)
    
    def put(self, endpoint: str, **kwargs) -> requests.Response:
        return self._request('PUT', endpoint, **kwargs)
    
    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        return self._request('DELETE', endpoint, **kwargs)