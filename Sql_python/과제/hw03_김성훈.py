import pymysql
import pandas as pd
def create_table(conn, cur, q):
    try:
        query = q
        cur.execute(query)
        conn.commit()
        print('Table 생성 완료')
    except Exception as e:
        print(e)
q1="""
            create table user_table
            (userID char(8) not null,
            username varchar(10) not null,
            birthYear INT not null,
            addr char(2) not null,
            mobile1 char(3),
            mobile2 char(8),
            height smallint,
            mDate date,
            constraint pk_user_table primary key(userID))
            """
q2="""create table buy_table
            (num int auto_increment not null,
            userID char(8) not null,
            prodName char(6) not null,
            groupName char(4) not null,
            price int not null,
            amount smallint not null,
            constraint pk_buy_table primary key(num),
            constraint fk_buy_table_userID foreign key(userID)
            references user_table(userID))
            """
        
def insert_manydata(conn,cur,d,s):
    try:
        cur = conn.cursor()
        sql = s
        
        data = d

        cur.executemany(sql, data)

        conn.commit()
        print('executemany 완료')
    except Exception as e:
        print(e)
d1=(('KHD', '강호동', 1970,'경북','011','22222222',182,'2007-07-07'),
    ('KJD', '김제동', 1974,'경남','','',173,'2013-03-03'),
    ('KKJ', '김국진', 1965,'서울','019','33333333',171,'2009-09-09'),
    ('KYM', '김용만', 1967,'서울','010','44444444',177,'2015-05-05'),
    ('LHJ', '이휘재', 1972,'경기','011','88888888',180,'2006-04-04'),
    ('LKK', '이경규', 1960,'경남','018','99999999',170,'2004-12-12'),
    ('NHS', '남희석', 1971,'충남','016','66666666',180,'2017-04-04'),
    ('PSH', '박수홍', 1970,'서울','010','00000000',183,'2012-05-05'),
    ('SDY', '신동엽', 1971,'경기','','',176,'2008-10-10'),
    ('YJS', '유재석', 1972,'서울','010','11111111',178,'2008-08-08')
    )
s1="""insert into user_table
            values (%s, %s, %s,%s,%s,%s,%s,%s)"""
d2=((1,'KHD', '운동화', '', 30, 2),
    (2,'KHD', '노트북', '전자', 1000, 1),
    (3,'KYM', '모니터', '전자', 200, 1),
    (4,'PSH', '모니터', '전자', 200, 5),
    (5,'KHD', '청바지', '의류', 50, 3),
    (6,'PSH', '메모리', '전자', 80, 10),
    (7,'KJD', '책', '서적', 15, 5),
    (8,'LHJ', '책', '서적', 15, 2),
    (9,'LHJ', '청바지', '의류', 50, 1),
    (10,'PSH', '운동화', '', 30, 2),
    (11,'LHJ', '책', '서적', 15, 1),
    (12,'PSH', '운동화', '', 30, 2)
    )
s2="""insert into buy_table
            values (%s, %s, %s,%s,%s,%s)"""

def select_table(conn,cur,s):
    try:
        cur = conn.cursor()
        sql = s

        cur.execute(sql)
        rows = cur.fetchall()	# 모든 데이터를 가져옴
        for row in rows:
            print(row)
        print(' ')
        conn.commit()

    except Exception as e:
        print(e)
sj="""select u.userName,b.prodName,u.addr,concat(u.mobile1,u.mobile2) 연락처
    from user_table as u
    inner join buy_table as b
    on u.userID=b.userID"""
suser="""select u.userID,u.userName,b.prodName,u.addr,concat(u.mobile1,u.mobile2) 연락처
    from user_table as u
    inner join buy_table as b
    on u.userID=b.userID
    where u.userID='KYM'"""
sorder="""select u.userID,u.userName,b.prodName,u.addr,concat(u.mobile1,u.mobile2) 연락처
    from user_table as u
    inner join buy_table as b
    on u.userID=b.userID
    order by u.userID;"""
sdis="""select distinct (u.userID),u.userName,u.addr
    from user_table as u
    inner join buy_table as b
    on u.userID=b.userID;"""
saddr="""select u.userID,u.userName,u.addr,concat(u.mobile1,u.mobile2) 연락처
    from user_table as u
    inner join buy_table as b
    on u.userID=b.userID
where u.addr in ('경북','경남');"""



def main():
    #데이터 베이스(sqlclass_db) 연결
    conn = pymysql.connect(host='localhost',
                        user='Cie', password='0422',
                        db='shoppingmall', charset='utf8')
    #cursor 객체 생성
    cur=conn.cursor()

    #테이블 생성 함수 호출
    # create_table(conn,cur,q1)
    # create_table(conn,cur,q2)

    #데이터 여러개 입력
    # insert_manydata(conn,cur,d2,s2)

    #데이터 update,delete
    # update_delete(conn,cur)

    #데이터 select
    print('문제 1번')
    print('-------------------------------------------------')
    print('userName prodName    addr    연락처	')
    print('-------------------------------------------------')
    select_table(conn,cur,sj)

    print('문제 2번')
    print('-------------------------------------------------')
    print('userID   userName   prodName    addr   연락처')
    print('-------------------------------------------------')
    select_table(conn,cur,suser)

    print('문제 3번')
    print('-------------------------------------------------')
    print('userID   userName   prodName    addr   연락처	')
    print('-------------------------------------------------')
    select_table(conn,cur,sorder)

    print('문제 4번')
    print('-------------------------------------------------')
    print('userID   userName  addr')
    print('-------------------------------------------------')
    select_table(conn,cur,sdis)

    print('문제 5번')
    print('-------------------------------------------------')
    print('userID   userName  addr	 연락처')
    print('-------------------------------------------------')
    select_table(conn,cur,saddr)

    #연결 종료
    cur.close()
    conn.close()
    print('Database 연결 종료')
main()