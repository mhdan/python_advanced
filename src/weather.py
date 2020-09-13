# this program tell the weather base on the internet!!!
import requests

# # API URL: https://api.openweathermap.org/
# # API key : 6fda8acfe9e56a5a641d37239ae09c0b


def sending_req(city):
    endpoint = 'https://api.openweathermap.org/data/2.5/weather'
    API_key = '6fda8acfe9e56a5a641d37239ae09c0b'

    templist = []
    for word in city.strip().split():
        templist.append(word[0].upper() + word[1:].lower())
    city_name = " ".join(templist)
    units = 'metric'
    lang = 'en'
    # city_id = '112931'
    paramerters = {
        'q': city_name,
        'appid': API_key,
        'units': units,
        'lang': lang
        # 'id': city_id,
    }

    try:
        r = requests.get(endpoint, paramerters)
        # next statement make code to raise exception if HTTP error happen
        r.raise_for_status()
    except requests.exceptions.Timeout:
        print("maybe your internet connection was interrupt\nplease check your internet connection and then try again!")
        exit(-1)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    return r.json()


def extracting_data(data):
    res_dict = dict()
    res_dict['city'] = data['name']
    # dic ['main'], ['description']
    res_dict['weather_main'] = data['weather'][0]['main']
    res_dict['weather_desc'] = data['weather'][0]['description']
    # dic ['temp'], ['feels_like'], ['temp_min'], ['temp_max']
    res_dict['temp_main'] = data['main']['temp']
    res_dict['temp_feels'] = data['main']['feels_like']
    res_dict['temp_max'] = data['main']['temp_max']
    res_dict['temp_min'] = data['main']['temp_min']

    res_dict['pressure'] = data['main']['pressure']         # dic ['pressure']
    res_dict['humidity'] = data['main']['humidity']         # dic ['humidity']

    # dic ['speed'], ['deg']
    res_dict['wind_speed'] = data['wind']['speed']
    # dic ['speed'], ['deg']
    res_dict['wind_deg'] = data['wind']['deg']

    return res_dict


def print_result(res_dic):
    print("+----------------------------------------------------------------------------------+")
    print("| City: {:^74} |".format(res_dic['city']))
    print("+----------------------------------------------------------------------------------+")
    print("| Weather:{:72} |\n|      main weather: {:>23} | description: {:>22} |"
          .format("", res_dic['weather_main'], res_dic['weather_desc']))
    print("+----------------------------------------------------------------------------------+")
    print("| Temperature:{:68} |\n|      mean temp: {:>6} | feel temp: {:>6} | max temp: {:>6} | min temp: {:>6} |"
          .format("", res_dic['temp_main'], res_dic['temp_feels'], res_dic['temp_max'], res_dic['temp_min']))
    print("+----------------------------------------------------------------------------------+")
    print("| Humidity:  {:28} | Pressure: {:28} |"
          .format(res_dic['humidity'], res_dic['pressure']))
    print("+----------------------------------------------------------------------------------+")
    print("| Wind: {:74} |\n|      wind speed: {:22} | wind direction: {:22} |"
          .format("", res_dic['wind_speed'], res_dic['wind_deg']))
    print("+----------------------------------------------------------------------------------+")
    # print("\n", raw_data['id'])


city_name = input("Enter your city:\n")
raw_data = sending_req(city_name)
item_dic = extracting_data(raw_data)
print_result(item_dic)
