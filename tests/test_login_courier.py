import helper
import requests
from data import Urls, ApiHandles, DataForTests


class TestLoginCourier:
    def test_login_existing_courier(self):
        payload = DataForTests.existing_user
        response = requests.post((Urls.main_site + ApiHandles.login_courier), data=payload)
        assert response.status_code == 200

    def test_login_without_password(self):
        payload = {"login": DataForTests.existing_user_login}
        response = requests.post((Urls.main_site + ApiHandles.login_courier), data=payload)
        assert response.status_code == 400

    def test_login_without_login(self):
        payload = {"password": DataForTests.existing_user_password}
        response = requests.post((Urls.main_site + ApiHandles.login_courier), data=payload)
        assert response.status_code == 400

    def test_login_with_incorrect_password_response_body(self):
        payload = {"login": DataForTests.existing_user_login,
                   "password": True}
        response = requests.post((Urls.main_site + ApiHandles.login_courier), data=payload).json()
        assert response["message"] == "Учетная запись не найдена"

    def test_login_without_password_response_body(self):
        payload = {"login": DataForTests.existing_user_login}
        response = requests.post((Urls.main_site + ApiHandles.login_courier), data=payload)
        try:
            r = response.json()
            assert r["message"] == "Недостаточно данных для входа"
        except Exception:
            raise AssertionError(f"Невозможно извлечь тело ответа. Код ответа: {response.status_code}")

    def test_login_with_incorrect_login_response_body(self):
        payload = {"login": "DataForTests.existing_user_login",
                   "password": DataForTests.existing_user_password}
        response = requests.post((Urls.main_site + ApiHandles.login_courier), data=payload).json()
        assert response["message"] == "Учетная запись не найдена"

    def test_successful_login_response_body(self):
        payload = DataForTests.existing_user
        response = requests.post((Urls.main_site + ApiHandles.login_courier), data=payload).json()
        assert response["id"] == 237682


