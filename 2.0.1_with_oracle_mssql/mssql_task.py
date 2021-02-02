from sqlalchemy import Column, String, DateTime,Float, create_engine
from sqlalchemy.orm import sessionmaker

db = create_engine('mssql+pymssql://user:password@ip:port/db_name?charset=utf8')

sql = """
			select LogOnName
			from AppUsers
"""

connection = db.connect()
result = connection.execute(sql)
length = 0
for row in result:
    length += 1
print(length)

