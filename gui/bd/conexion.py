import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="feriavirtual",
    port=3308
)

cursor = database.cursor()

print(database)