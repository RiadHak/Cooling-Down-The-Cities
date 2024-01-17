import mysql.connector
from mysql.connector import errorcode
from datetime import datetime
def connectmysql(message):
    
    try:
        connection = mysql.connector.connect(
            password = 'password',
            user = 'root',
            host = '127.0.0.1',
            database = 'cdtcdb',
        )
        if connection:
            table = "dashboard_seeders"
            cursor = connection.cursor()
            keys = ', '.join(message.keys())
            keys += ", timestamp"
            values = tuple((message.values()))
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            values += time,
            add_message = f"INSERT INTO {table} ({keys}) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(add_message, values)
            connection.commit()
            connection.close()
        
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('password or user is wrong')
        elif error.errno == errorcode.ER_BAD_DB_ERROR:
            print('database doesnt exist')
        else:
            print(error)
        
    else:
        connection.close()
    return connection