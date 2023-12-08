import json
import os

import allure
import requests
from allure_commons.types import AttachmentType
from requests import Response
from selene.support.conditions import have
from selene.support.shared import browser

URL = 'https://demowebshop.tricentis.com'
user_agent = {'User-agent': 'Mozilla/5.0'}

def test_login_through_api():
    url = URL + '/login'

    with allure.step('login on site'):
        login_payload = {
            'Email': os.getenv('EMAIL'),
            'Password': os.getenv('PASSWORD'),
            'RememberMe': False
        }
        response = requests.post(url=url, data=login_payload, allow_redirects=False, headers=user_agent)
        assert response.status_code == 200
        #print(json.dumps(response.json()))
        allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True),
                      name="Response login", attachment_type=AttachmentType.JSON, extension="json")
    with allure.step('getting cookies'):
        cookies = response.cookies.get('NOPCOMMERCE.AUTH')

    with allure.step('set cookies on browser'):
        browser.open(URL)
        browser.driver.add_cookie({'name': "NOPCOMMERCE.AUTH", 'value': cookies})
        browser.open(URL)
    with allure.step('browser should have my name on page'):
        browser.element('.account').should(have.text(os.getenv('EMAIL')))


def test_add_laptop_to_cart():
    url = URL + '/addproducttocart/catalog/31/1/1'

    with allure.step('adding to cart a laptop on main page'):
        response: Response = requests.post(url=url)
        allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True),
                      name="Response adding a product to cart", attachment_type=AttachmentType.JSON, extension='json')

    with allure.step('checking cart for added product'):
        browser.element('.ico-cart').click()
        browser.element('.cart-item-row').should(have.text('14.1-inch Laptop'))


def test_add_cheap_computer_to_card():
    url = URL + '/addproducttocart/details/72/1'
    payload_json = {
        "product_attribute_72_5_18": 53,
        "product_attribute_72_6_19": 54,
        "product_attribute_72_3_20": 57,
        "addtocart_72.EnteredQuantity": 1
    }

    with allure.step('adding to cart a cheap computer with parameters'):
        response: Response = requests.post(url=url, json=payload_json)
        allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True),
                      name="Response adding a product to cart", attachment_type=AttachmentType.JSON, extension='json')

    with allure.step('checking cart for added product'):
        browser.element('.ico-cart').click()
        browser.element('.cart').should(have.text('Build your own cheap computer'))
