import helper
import requests
from data import Urls, ApiHandles, DataForTests


class TestGetOrderByTrack:
    def test_get_order_returns_object(self):
        track = helper.create_order_return_track()
        response = requests.get(f'{Urls.main_site}{ApiHandles.get_order_id}?t={track}').json()
        assert isinstance(response["order"], dict)
        helper.close_order(response["order"]["id"])

    def test_get_order_without_track(self):
        response = requests.get(f'{Urls.main_site}{ApiHandles.get_order_id}?t=').json()
        assert response["message"] == "Недостаточно данных для поиска"

    def test_get_order_with_unexisting_track(self):
        track = helper.generate_random_number()
        response = requests.get(f'{Urls.main_site}{ApiHandles.get_order_id}?t={track}').json()
        assert response["message"] == "Заказ не найден"


