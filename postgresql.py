import psycopg2 
import psycopg2.extras

con=psycopg2.connect(
    user='postgres',
    dbname='practice',
    host='localhost',
    password='8227',
    port=5432
    )

cur=con.cursor(cursor_factory=psycopg2.extras.DictCursor)

cur.execute('DROP TABLE IF EXISTS friends')
table='''  CREATE TABLE IF NOT EXISTS friends(

    name        VARCHAR(20) PRIMARY KEY,

    age         INT NOT NULL ,

    dptment     VARCHAR(20),

    period      INT


)'''

cur.execute(table)


script='''INSERT INTO friends VALUES(%s,%s,%s,%s)'''
values=[('manikandan',23,'ECE',23),('Shanmugaraja',22,'MECH',22),('GOKUL',23,'ECE',4)]


for value in values:
    cur.execute(script,value)


update=cur.execute('UPDATE friends SET age=56 WHERE name =\'Shanmugaraja\'')

cur.execute('DELETE FROM friends WHERE period=4 ')
cur.execute('select * from friends')
for i in (cur.fetchall()):
    
    print(i['name'],i['age'])



con.commit()




cur.close()
con.close()