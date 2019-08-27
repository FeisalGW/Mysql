# menghubungkan python ke mysql
# pip install mysql-connecto-python #

import mysql.connector

dbku = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'feisal',
    passwd = '1616',
    auth_plugin = 'mysql_native_password',
    database = 'doraemon'

)
print(dbku)

#check database
kursor = dbku.cursor()
data = [
    ('shizuka',12),
    ('suneo',12)
]
query = '''insert into karakter(nama, usia)
values (%s,%s)'''
kursor.executemany('querydb, data')  #untuk bikin data di database, tnpa lewat mysql
dbku.commit
(print(kursor.rowcount, 'data baru tersimpan'))

import mysql.connector

dbku = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'feisal',
    passwd = '1616',
    auth_plugin = 'mysql_native_password',
    database = 'doraemon'

)
print(dbku)

#ambil database
kursor = dbku.cursor()
querydb = '''select * from karakter'''
kursor.execute(querydb)  

print(kursor.fetchall())
print(kursor.fetchone())
print(kursor.fetchmany(2))

#cara update data
kursor = dbku.cursor()
querydb = '''update karakter set
nama = %s where nama = %s'''
data = ('Goda takeshi','giant')
kursor.execute(querydb, data)
dbku.commit
print(kursor.rowcount, 'data terupdate!')