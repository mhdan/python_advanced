# this is program to search in tehran's divar for given laptop

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil import tz
import mysql.connector
from mysql.connector import errorcode


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
    res_list.append(datetime.now(tz=tz.tzlocal()))
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


def storing_in_databse(list_of_dictes):
    try:
        print("connecting to mysql database")
        cnx = mysql.connector.connect(user='me_learning', password='Mohammad@1377',
                                      host='127.0.0.1', database='learn')
        cursor = cnx.cursor()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("something is wrong with username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        print("connected to mysql database")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS learn.divar ( search_date VARCHAR(40), name VARCHAR(70), price VARCHAR(20), location VARCHAR(70), link VARCHAR(200));")
        # create table if doesn't exist !!!
        sq1 = "INSERT INTO divar (search_date, name, price, location, link) VALUES (%s, %s, %s, %s, %s)"
        for each_dict in list_of_dictes[1:]:
            this_row = [list_of_dictes[0], each_dict['name'],
                        each_dict['price'], each_dict['location'], each_dict['link']]
            cursor.execute(sq1, this_row)
        cnx.commit()
    finally:
        cursor.close()
        cnx.close()


def printing_result(list_of_dictes):
    print(f"date of search: {list_of_dictes[0]}\n")
    for each_dic in list_of_dictes[1:]:
        print("name: %s\nprice: %s\nlocation: %s\nlink: %s"
              % (each_dic['name'], each_dic['price'], each_dic['location'], each_dic['link']))
        print("---------------------------------------------------")


search_item, price = get_data_from_user()
text_data = sending_req(search_item, price)
list_of_dictes = extracting_data(text_data)
storing_in_databse(list_of_dictes)
printing_result(list_of_dictes)
