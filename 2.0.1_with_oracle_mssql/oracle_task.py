import datetime

from sqlalchemy import Column, String, DateTime,Float, create_engine
from sqlalchemy.orm import sessionmaker



db_engine = create_engine('oracle://user:password@ip:port/db_name')

db_session = sessionmaker(bind=db_engine)
session = db_session()

sql = """
			select trim(A.item) as item
			from bo_read898.tcibd001 A
			where A.kitm = '2'
			and (trim(A.item) not like 'HPM%'
			and trim(A.item) not like 'DEL%'
			and trim(A.item) not like 'LNV%')
			and (A.csig = 'IAI' or A.csig = '   ' or A.csig = 'CAH')

"""

connection = db_engine.connect()
result = connection.execute(sql)
length = 0
for row in result:
    length += 1
print(length)

