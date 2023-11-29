import requests
import pytest
from data import Urls, ApiHandles, DataForTests


class TestGetOrdersList:
    def test_get_orders_list_response(self):
        response = requests.get(Urls.main_site + ApiHandles.get_orders_list).json()
        assert isinstance(response["orders"], list)

