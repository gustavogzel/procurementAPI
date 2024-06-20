from sqlalchemy import create_engine
from datetime import datetime
import psycopg2
import os

#export IP_DB=127.0.0.1
ip_databse = os.environ['IP_DB']

#INPUT YOUR OWN CONNECTION STRING HERE
conn_string = 'postgresql://pstguser:pstg123@'+ip_databse+'/contrataciones'

pg_conn = psycopg2.connect(conn_string)
cur = pg_conn.cursor()

#cur.execute('SELECT count(*),contract."Plantilla del expediente" FROM contract group by contract."Plantilla del expediente" order by 1 desc')
#cur.execute('SELECT sum("Importe del contrato"),contract."Siglas de la Institución" FROM contract group by contract."Siglas de la Institución" order by 1 desc limit 20')
cur.execute('SELECT sum("Importe del contrato"),TO_CHAR(contract."Fecha de inicio del contrato",\'Month\'),EXTRACT(month from contract."Fecha de inicio del contrato")as m FROM contract group by TO_CHAR(contract."Fecha de inicio del contrato",\'Month\'),EXTRACT(month from contract."Fecha de inicio del contrato") ORDER BY EXTRACT(month from contract."Fecha de inicio del contrato")')


rows = cur.fetchall()
for row in rows:
    print(row)