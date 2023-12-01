import helper
import requests
from data import Urls, ApiHandles, DataForTests


class TestCreateCourier:
    def test_create_courier_success_response_code(self):
        login, password, first_name = helper.generate_login_pass_first_name()
        login_pass = []
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post((Urls.main_site + ApiHandles.create_courier), data=payload)
        assert response.status_code == 201 and response.json() == {"ok": True}
        print(response.json())
        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)
            courier_id = helper.login_existing_courier(login_pass)
            helper.delete_courier(courier_id)

    def test_create_courier_which_already_exist(self):
        payload = DataForTests.existing_user
        response = requests.post((Urls.main_site + ApiHandles.create_courier), data=payload)
        print(response.json())
        assert response.status_code == 409 and response.json()["message"] == "Этот логин уже используется"

    def test_create_courier_with_login_and_pass_only_success(self):
        login = helper.generate_random_string(10)
        password = helper.generate_random_string(10)
        login_pass = []
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post((Urls.main_site + ApiHandles.create_courier), data=payload)
        assert response.status_code == 201 and response.json() == {"ok": True}
        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            courier_id = helper.login_existing_courier(login_pass)
            helper.delete_courier(courier_id)

    def test_successful_courier_creation_response_body(self):
        login, password, first_name = helper.generate_login_pass_first_name()
        login_pass = []
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post((Urls.main_site + ApiHandles.create_courier), data=payload)
        response_body = response.json()
        assert response_body == {"ok": True}
        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)
            courier_id = helper.login_existing_courier(login_pass)
            helper.delete_courier(courier_id)

    def test_create_courier_with_login_only_fail(self):
        login = helper.generate_random_string(10)
        first_name = helper.generate_random_string(10)
        payload = {
            "login": login,
            "firstName": first_name
        }
        response = requests.post((Urls.main_site + ApiHandles.create_courier), data=payload)
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для создания учетной записи"

    def test_create_courier_with_pass_only_fail(self):
        password = helper.generate_random_string(10)
        first_name = helper.generate_random_string(10)
        payload = {
            "password": password,
            "firstName": first_name
        }
        response = requests.post((Urls.main_site + ApiHandles.create_courier), data=payload)
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для создания учетной записи"

    def test_create_courier_existing_login(self):
        login = DataForTests.existing_user_login
        password = helper.generate_random_string(10)
        first_name = helper.generate_random_string(10)
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post((Urls.main_site + ApiHandles.create_courier), data=payload)
        assert response.status_code == 409 and response.json()["message"] == "Этот логин уже используется"
