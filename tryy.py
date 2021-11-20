import psycopg2 

host='localhost'
db='punish'
user='postgres'
pwd='8227'
port=5432

try:

        conn=psycopg2.connect(
            host=host,
            database=db,
            user=user,
            password=pwd,
            port=port
            )

        cur=conn.cursor()
        cur.execute('DROP TABLE IF EXISTS victims')

        script=''' CREATE TABLE IF NOT EXISTS victims(
            id          int PRIMARY KEY,
            name        varchar(50) NOT NULL,
            date        varchar(20),
            punish      varchar(100) NOT NULL
        )'''
        cur.execute(script)
        
        
        #inserting data
        table_data='INSERT INTO victims (id,name,date,punish) VALUES (%s,%s,%s,%s)'
        data=(1,'sudha','27/12/2021','kirumibojanam')
       
        cur.execute(table_data,data)

       
        conn.commit()



       
except Exception as e:
    print(e)

finally:
  if conn is not None:
    conn.close()
  if cur is not None:
    cur.close()

