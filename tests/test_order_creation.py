import json

import helper
import requests
import pytest
from data import Urls, ApiHandles, DataForTests


class TestOrderCreation:
    @pytest.mark.parametrize('color', [["GREY"], ["BLACK"], ["GREY", "BLACK"], []])
    def test_create_order_with_different_colors(self, color):
        order_data = DataForTests.order_data
        order_data["color"] = color
        payload_string = json.dumps(order_data)
        response = requests.post((Urls.main_site + ApiHandles.create_order), data=payload_string)
        assert response.status_code == 201

    def test_successful_order_creation_response_body(self):
        payload_string = json.dumps(DataForTests.order_data)
        response = requests.post((Urls.main_site + ApiHandles.create_order), data=payload_string).json()
        print(response["track"])
        assert response["track"] is not None

