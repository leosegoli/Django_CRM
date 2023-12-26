import mysql.connector


dataBase = mysql.connector.connect(
    host= 'localhost',
    user = 'root',
    passwd= 'Leosegoli1984',
    auth_plugin='mysql_native_password'
)


cursorOBject = dataBase.cursor()

cursorOBject.execute("CREATE DATABASE eldercode")

print("All Done!")