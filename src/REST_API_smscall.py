# A program to call api and then after comutiing, base on res send SMS with REST_API
import requests

my_good_price = 11000


def get_Bit_price():
    r_coinbase = requests.get('https://api.coinbase.com/v2/prices/buy?currency=USD')
    price = float(r_coinbase.json()['data']['amount'])
    print(f"the price of each Bitcoin to buy is {price} dollors!!!")
    return price


def inform_mohammad(price):
    API_Key_for_KavehNegar = "55555A62746E614B427539784D45654B4A325256794B537531682F7474516535474A4E4659326A756F6A493D"
    url = f'https://api.kavenegar.com/v1/{API_Key_for_KavehNegar}/sms/send.json'
    payload = {
        'receptor': '09365972227',
        'message': f'the Bit price is {price} at this moment!\nhurry to buy it NOW!!!'
    }
    r_kaveh = requests.post(url, data=payload)
    return r_kaveh.status_code


price = get_Bit_price()
if price < my_good_price:
    print('inform mohammad, this the time to buy!!!')
    print(inform_mohammad(price))
else:
    print('still to expensive!!')
