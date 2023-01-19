# ----------------------------------------------------------
# list, tuple => 저장 순서대로 파이썬 번호 부여 인덱스
# ----------------------------------------------------------
data='1 2 3 4 5'#type-str
data=data.split()#type-list


# ----------------------------------------------------------
# dict => {key : value, key: value,....}
# key로 값 사용, key 중복 X => 만약에 중복되면 값 변경
# ----------------------------------------------------------

person={'name':'ss',12:'num',12:'good'}
keys=person.keys()
v=person.values()
print(keys,v,person[12])
for i in keys:
    print(i)
#키 값 묶음 items()
dd=person.items()
print(dd)
#언팩킹 => 묶음 풀기
for x,y in dd:
    print(x,y)
#추가하기
person['주차비']='겁나비싸'
print(person)


