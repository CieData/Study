import pymysql
import pandas as pd

conn = pymysql.connect(host='localhost', user='Cie',	
                        password='0422',
                        db = 'sakila', charset='utf8')
cur = conn.cursor()
cur.execute('select	* from language')
rows = cur.fetchall()	# 모든 데이터를 가져옴
print(rows)
language_df = pd.DataFrame(rows)	# DataFrame 형태로 변환
print(language_df)

query = """select c.email
from customer as c
    inner join rental as r	
    on c.customer_id = r.customer_id
where date(r.rental_date) = (%s)"""

cur.execute(query, ('2005-06-14'))
rows = cur.fetchall()	# 모든 데이터를 가져옴
rows
for row in rows:
    print(row)
cur.close()
conn.close()