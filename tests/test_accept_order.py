import helper
import requests
from data import Urls, ApiHandles, DataForTests


class TestAcceptOrder:
    def test_successful_accept_order_response_body(self):
        order_id = helper.get_new_order_id_by_track()
        response = requests.put(f'{Urls.main_site}{ApiHandles.accept_order}{order_id}?courierId={DataForTests.existing_user_id}').json()
        assert response == {"ok": True}
        helper.close_order(order_id)

    def test_accept_order_without_courier_id(self):
        order_id = helper.get_new_order_id_by_track()
        response = requests.put(f'{Urls.main_site}{ApiHandles.accept_order}{order_id}?courierId=').json()
        assert response["message"] == "Недостаточно данных для поиска"
        helper.close_order(order_id)

    def test_accept_order_with_unexisting_courier_id(self):
        order_id = helper.get_new_order_id_by_track()
        response = requests.put(f'{Urls.main_site}{ApiHandles.accept_order}{order_id}?courierId={DataForTests.extra_long_courier_id}').json()
        assert response["message"] == "Курьера с таким id не существует"

    def test_accept_order_without_order_id(self):
        order_id = helper.get_new_order_id_by_track()
        response = requests.put(f'{Urls.main_site}{ApiHandles.accept_order}?courierId={DataForTests.existing_user_id}').json()
        assert response["message"] == "Недостаточно данных для поиска"
        helper.close_order(order_id)

    def test_accept_order_with_unexisting_order_id(self):
        order_id = helper.generate_unexisting_order_id()
        response = requests.put(
            f'{Urls.main_site}{ApiHandles.accept_order}{order_id}?courierId={DataForTests.existing_user_id}').json()
        assert response["message"] == "Заказа с таким id не существует"
