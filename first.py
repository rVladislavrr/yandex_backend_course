import requests

BASE_URL = 'https://fakestoreapi.com/'


def get_product_price(price: int = 20):
    response = requests.get(url=BASE_URL + 'products').json()
    print([product for product in response if product.get('price') < price])


def get_all_categories():
    response = requests.get(url=BASE_URL + 'products/categories').json()
    print(response)


def get_all_products_in_category(category: str = 'jewelery'):
    response = requests.get(url=BASE_URL + 'products/category/' + category).json()
    print(response)


def get_all_users():
    response = requests.get(url=BASE_URL + 'users').json()
    print(response)


def __get_user_id(index: int):
    response = requests.get(BASE_URL + f'users/{index}').json()
    return response


def create_user():
    user = {
        'email': 'VladislavLavrov@gmail.com',
        'username': 'VladislavLavrov',
        'password': 'qwerty',
        'name': {
            'firstname': 'Vladislav',
            'lastname': 'Lavrov'
        },
        'address': {
            'city': 'Yekaterinburg',
            'street': 'Mira Street',
            'number': 19,
            'zipcode': '620002',
            'geolocation': {
                'lat': '56.84403',
                'long': '60.654077'
            }
        },
        'phone': '812345678900'
    }
    response = requests.post(BASE_URL + 'users', user)
    if response.status_code == 200:
        res = __get_user_id(response.json().get('id'))
        print(res)
        return
    raise Exception("Пользователь не создался")


if __name__ == '__main__':
    get_product_price()
    get_all_categories()
    get_all_products_in_category()
    get_all_users()
    create_user()
