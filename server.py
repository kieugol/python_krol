import mysql.connector

try:
  cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='krol')
  cursor = cnx.cursor()
  cursor.execute("SELECT * FORM user")
  cnx.close()
except mysql.connector.Error as err:
  print("Something went wrong: {}".format(err))