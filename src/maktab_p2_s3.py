import mysql.connector
from mysql.connector import errorcode

person = ('reza', 'm', 28)

# ****** inserting new row to mysql **********

# # trying to connect to mysql server
# try:
#     print("connecting to mysql database")
#     cnx = mysql.connector.connect(user='me_learning', password='Mohammad@1377',
#                                   host='127.0.0.1',
#                                   database='learn')
#     # initilaize the cursor
#     cursor = cnx.cursor()
# # if error happen on connecting do these
# except mysql.connector.Error as err:
#     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#         print("something is wrong with username or password")
#     elif err.errno == errorcode.ER_BAD_DB_ERROR:
#         print("Database does not exist")
#     else:
#         print(err)
# # if successfully connected, do these
# else:
#     print("connected to mysql database")
#     # notice: %s in mysql is different with %s in python formating!!!
#     # notice: always with params in mysql should use %s
#     sq1 = "INSERT INTO people (name, sex, age) VALUES (%s, %s, %s)"
#     # run the following command with .execute()
#     # give command on first and data in seocond params!
#     cursor.execute(sq1, person)

#     # # we can give data as params or in one string command!!!
#     # # we can use below code also!!!
#     # cursor.execute("INSERT INTO people VALUES ('%s', '%s', %i)" %
#     #                (person[0], person[1], person[2]))

#     # make sure the changes happened!!!!!
#     cnx.commit()
# # always do these
# finally:
#     cursor.close()
#     cnx.close()

###############################################

# ******* reading from mysql *****

# trying to connect to mysql server
try:
    print("connecting to mysql database")
    cnx = mysql.connector.connect(user='me_learning', password='Mohammad@1377',
                                  host='127.0.0.1',
                                  database='learn')
    # initilaize the cursor
    cursor = cnx.cursor()
# if error happen on connecting do these
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("something is wrong with username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
# if successfully connected, do these
else:
    print("connected to mysql database")

    # reading all rows of people table
    query1 = "SELECT * FROM people"
    cursor.execute(query1)
    for row in cursor:
        print(row)
    # reading name and age of rows between start and finish
    query2 = "SELECT name, age FROM people WHERE age BETWEEN %s AND %s"
    start = 20
    finish = 25
    cursor.execute(query2, (start, finish))
    for name, age in cursor:
        print("%s is %i years old!" % (name, age))
# always do these
finally:
    cursor.close()
    cnx.close()
