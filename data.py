class Urls:
    main_site = 'https://qa-scooter.praktikum-services.ru'


class ApiHandles:
    login_courier = '/api/v1/courier/login'
    create_courier = '/api/v1/courier'
    delete_courier = '/api/v1/courier/'
    create_order = '/api/v1/orders'
    get_orders_list = '/api/v1/orders'
    close_order = '/api/v1/orders/finish/'
    accept_order = '/api/v1/orders/accept/'
    get_order_id = '/api/v1/orders/track'


class DataForTests:
    existing_user = {
        "login": "existing_user",
        "password": "1234",
        "firstName": "marty"}

    existing_user_login = "existing_user"
    existing_user_password = "1234"
    existing_user_id = "237682"

    order_data = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": []
    }
    extra_long_courier_id = "1234567890"

