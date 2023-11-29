import requests
import random
import string
import json
from data import Urls, ApiHandles, DataForTests


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_login_pass_first_name():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    return login, password, first_name


def generate_random_number():
    return random.randint(1000000, 9999999)


def login_existing_courier(login_pass):
    payload = {
        "login": login_pass[0],
        "password": login_pass[1]
    }
    response = requests.post((Urls.main_site + ApiHandles.login_courier), data=payload)
    if response.status_code == 200:
        r = response.json()
        return r["id"]


def register_new_courier_and_return_login_password():
    login_pass = []
    login, password, first_name = generate_login_pass_first_name()

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = requests.post((Urls.main_site + ApiHandles.create_courier), data=payload)
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass


def delete_courier(courier_id):
    requests.delete(Urls.main_site + ApiHandles.delete_courier + str(courier_id))


def create_order_return_track():
    payload_string = json.dumps(DataForTests.order_data)
    response = requests.post((Urls.main_site + ApiHandles.create_order), data=payload_string)
    if response.status_code == 201:
        return response.json()["track"]


def get_new_order_id_by_track():
    track = create_order_return_track()
    response = requests.get(f'{Urls.main_site}{ApiHandles.get_order_id}?t={track}').json()
    return response["order"]["id"]



def close_order(order_id):
    response = requests.put(Urls.main_site + ApiHandles.close_order + str(order_id))


def generate_unexisting_order_id():
    response = requests.get(Urls.main_site + ApiHandles.get_orders_list).json()
    orders_list = response["orders"]
    print(orders_list)
    random_id = 0
    while True:
        random_id = generate_random_number()
        print(random_id)
        flag = True
        for i in range(len(orders_list)):
            if random_id == orders_list[i]["id"]:
                break
            else:
                flag = False
        if flag == False:
            break
    return random_id
