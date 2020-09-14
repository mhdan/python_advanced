# this is program to search in tehran's divar for given laptop

import requests
from bs4 import BeautifulSoup


def get_data_from_user():
    laptop = input("Enter your laptop name:\n")
    low_price = input(
        "Enter your down limit in price :\n(live it blank, if you don't have any limit)\n")
    high_price = input(
        "Enter your up limit in price :\n(live it blank, if you don't have any limit)\n")
    if low_price or high_price:
        final_price = '-'.join([low_price, high_price])
    else:
        final_price = ""
    return laptop, final_price


def sending_req(search, price):
    endpoint = "https://divar.ir/s/tehran/laptop-notebook-macbook"
    parameters = {
        'q': search,
        'price': price
    }

    try:
        r = requests.get(endpoint, parameters)
        # next statement make code to raise exception if HTTP error happen
        r.raise_for_status()
    except (requests.Timeout, requests.ConnectionError):
        # catch timeout error!
        print("maybe your internet connection was interrupt\nplease check your internet connection and then try again!")
        exit(-1)
    except requests.RequestException as e:
        raise SystemExit(e)
    except requests.HTTPError as err:
        raise SystemExit(err)

    return r.text


def extracting_data(text_data):
    soup = BeautifulSoup(text_data, 'html.parser')
    # print(soup.prettify())
    items_list = soup.find_all(
        'a', attrs={'class': 'kt-post-card kt-post-card--outlined kt-post-card--bordered'})
    res_list = []
    for item in items_list:
        name = item.find(
            'div', attrs={'class': 'kt-post-card__title'}).text    # name
        price = item.find('div', attrs={
            'class': 'kt-post-card__top-description kt-post-card-description'}).text  # price
        location = item.find('div', attrs={
            'class': 'kt-post-card__bottom-description-wrapper'}).text  # location
        link = "https://divar.ir" + item.attrs['href']
        item_dic = {
            'name': name,
            'price': price,
            'location': location,
            'link': link
        }
        res_list.append(item_dic)

    return res_list


def printing_result(list_of_dictes):
    for each_dic in list_of_dictes:
        print("name: %s\nprice: %s\nlocation: %s\nlink: %s"
              % (each_dic['name'], each_dic['price'], each_dic['location'], each_dic['link']))
        print("---------------------------------------------------")


search_item, price = get_data_from_user()
text_data = sending_req(search_item, price)
list_of_dictes = extracting_data(text_data)
printing_result(list_of_dictes)
