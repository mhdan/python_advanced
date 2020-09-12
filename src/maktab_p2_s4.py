import re
# name and family regex = "^\s*((\b\w+)(\s*(\b\w+))*)\s+(\b\w+)$""


# # notice: 'r' ghabl az regex yani mesl charachter mamoli dar nazar begir,
# # notice: r'\n' dige be mana khat bad nist!!!
# # notice: yani escap cahr ha faghat escaphaye regex hastan va mal string nist!!!

# # .searh() method only find first accurance!
# txt = "The rain in Spain"
# x = re.search(r"\s.", txt)
# print(x)
# print(x.span())
# print(x.string)
# print(x.group())
# #
# # output: <re.Match object; span=(3, 5), match=' r'>
# # output: (3, 5)
# # output: The rain in Spain
# # output:  r

###############################################

# txt = "The rain in Spain"
# y = re.findall(r"ai", txt)
# print(y)
# #
# # output: ['ai', 'ai']

###############################################

# txt = "The rain in Spain"
# x = re.split(r"i", txt, maxsplit=2)
# print(x)
# #
# # output: ['The ra', 'n ', 'n Spain']

###############################################

# # .sub() method wil replace matched parts with given string!
# txt = "The rain in Spain"
# x = re.sub(r"\s", "9", txt, count=2)
# print(x)
# #
# # output: The9rain9in Spain

###############################################

# # same as .sub() but return tuple with number of replacement have done!
# string = 'abc 12\
# de 23 \n f45 6'
# pattern = r'\s+'
# replace = ''
# new_string = re.subn(pattern, replace, string)
# print(new_string)
# #
# # output: ('abc12de23f456', 4)

###############################################

# enterSrting = '''the price of oil is 30$ per 1 boshkeh for yesterday,
# the price of oil is 58$ per 1 boshkeh for today,
# the price of oil is 43$ per 1 boshkeh for tomorrow.'''

# result = re.findall(r"the price of oil is (\d+)\$ per (\d+) boshkeh for (\w+)", enterSrting)
# print(result)
# #
# # output: [('30', '1', 'yesterday'), ('58', '1', 'today'), ('43', '1', 'tomorrow')]

###############################################

# enterSrting = '''khsoflhsdlj.768990@gmail.com
# sd;lifhsl;kg@yojs.deg
# s;jjfdsidflj@slid.rt
# sldjflsdjfdsfsdfsd@yahoo.org
# skdfhisdfnsd;@hohal.seijg'''

# given_regex = r"\b(.+)@(.+)\.(.{2,3})\b"
# result = re.sub(given_regex, "\g<1>@ui.ac.\g<3>+ir", enterSrting)
# print(result)
# #
# # output: khsoflhsdlj.768990@ui.ac.com+ir
# # output: sd;lifhsl;kg@ui.ac.deg+ir
# # output: s;jjfdsidflj@ui.ac.rt+ir
# # output: sldjflsdjfdsfsdfsd@ui.ac.org+ir
# # output: skdfhisdfnsd;@hohal.seijg
# # notice: "\g<>" is for using specific group of reg that matched!

###############################################

# enterString = ''' ali ashkani
#   	mohammad ziaei
# asghar mortezaei

#  mir ali reza kashani

# amir hosein ziaei
# '''

# regex = r"(\b\w+([\t ]+\b\w+)*)\s+(\b\w+)\n"
# result = re.findall(regex, enterString)
# for item in result:
#     print("the name is {:15s} and family is {:10s}!".format(item[0], item[2]))
# #
# # output: the name is ali             and family is ashkani   !
# # output: the name is mohammad        and family is ziaei     !
# # output: the name is asghar          and family is mortezaei !
# # output: the name is mir ali reza    and family is kashani   !
# # output: the name is amir hosein     and family is ziaei     !

###############################################
###############################################

import requests

# # API URL: https://api.livecoin.net/

# # requests.get(url, params={key: value}, args)
# # requests.get(url, auth = ('user', 'pass'))

# r = requests.get("https://api.livecoin.net/exchange/ticker?currencyPair=BTC/USD")
# print(r.status_code)
# print("the type is :%s -> %s" %(type(r.text), r.text))
# # json is same as dict in python :)
# j = r.json()
# print("the type is :%s -> %s" %(type(j), j))
# print("max value is %s and min is %s" %(j['high'], j['low']))

###############################################
