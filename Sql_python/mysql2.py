import pymysql
def create_table(conn, cur):
    try:
        query = """
            create table customer
            (name varchar(10),
            category smallint,	
            region varchar(10))
            """
        cur.execute(query)
        conn.commit()
        print('Table 생성 완료')
    except Exception as e:
        print(e)
        
def insert_manydata(conn,cur):
    try:
        curs = conn.cursor()
        sql = """insert into customer(name, category, region)
            values (%s, %s, %s)"""
        
        data = (('홍진우', 1, '서울'),
                ('강지수', 2, '부산'),
                ('김청진', 1, '대구'),
                )

        curs.executemany(sql, data)

        conn.commit()
        print('executemany 완료')
    except Exception as e:
        print(e)

def insert_table(conn,cur):
    try:
        curs = conn.cursor()
        sql = """insert into customer(name, category, region)
            values (%s, %s, %s)"""

        curs.execute(sql, ('홍길동', 1, '서울'))
        curs.execute(sql, ('이연수', 2, '서울'))

        conn.commit()
        print('INSERT 완료')

    except Exception as e:
        print(e)

def update_delete(conn,cur):
    try:
        curs = conn.cursor()
        sql = """update customer
            set region = '서울특별시'
            where region = '서울'"""

        #update 데이터
        curs.execute(sql)
        conn.commit()
        print('update 완료')

        #delete 데이터
        sql = "delete from customer where name=%s"
        curs.execute(sql, '홍길동')
        conn.commit()
        print('delete 홍길동')

    except Exception as e:
        print(e)

def main():
    #데이터 베이스(sqlclass_db) 연결
    conn = pymysql.connect(host='localhost',
                        user='Cie', password='0422',
                        db='sqlclass_db', charset='utf8')
    #cursor 객체 생성
    cur=conn.cursor()

    #테이블 생성 함수 호출
    create_table(conn,cur)

    # #데이터 입력
    # insert_table(conn,cur)

    # #데이터 여러개 입력
    # insert_manydata(conn,cur)

    # #데이터 update,delete
    # update_delete(conn,cur)

    #연결 종료
    cur.close()
    conn.close()
    print('Database 연결 종료')
main()