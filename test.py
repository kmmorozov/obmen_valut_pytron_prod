import pymysql

connection = pymysql.connect(host='192.168.20.24', user='obmen', password='123456', database='bank', port=3306)
cursor = connection.cursor()
cursor.execute('ALTER TABLE bank.valute_rate MODIFY COLUMN rate varchar(8) CHARACTER SET latin1 COLLATE latin1_swedish_ci DEFAULT NULL NULL;')

data = cursor.fetchall()

print(data)
