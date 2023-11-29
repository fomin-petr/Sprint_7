import helper
import requests
from data import Urls, ApiHandles, DataForTests


class TestDeleteCourier:
    def test_delete_courier_without_id(self):
        response = requests.delete(Urls.main_site + ApiHandles.delete_courier)
        assert response.status_code == 400

    def test_successful_delete_courier_response_body(self):
        login_pass = helper.register_new_courier_and_return_login_password()
        courier_id = helper.login_existing_courier(login_pass)
        response = requests.delete(Urls.main_site + ApiHandles.delete_courier + str(courier_id)).json()
        assert response == {"ok": True}

    def test_delete_courier_without_id_response_body(self):
        response = requests.delete(Urls.main_site + ApiHandles.delete_courier).json()
        assert response["message"] == "Недостаточно данных для удаления курьера"

    def test_delete_unexisting_courier_response_body(self):
        response = requests.delete(Urls.main_site + ApiHandles.delete_courier + str(DataForTests.extra_long_courier_id)).json()
        assert response["message"] == "Курьера с таким id нет"
