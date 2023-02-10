raw_data = read.csv(file='titanic_data.csv',header=T)
#12. head 함수를 사용하여 입력된 raw_data를 확인하시오.
head(raw_data)
#13. raw_data의 자료의 차원을 구하시오.
dim(raw_data)
#14. raw_data에서 성별(Sex)을 추출하고 gender.txt로 저장하시오.
write.table(raw_data['Sex'],file="gender.txt")
#15. raw_data의 2~10 열의 변수를 선택하여 새로운 객체에 저장하고 sub_data.txt로 저장하시오.(구분은 _을 이용할 것)
titanic = raw_data[,2:10]
write.table(titanic,file="sub_data.txt", sep='_')
#16. raw_data의 31~100의 행과 2~10 사이의 짝수 열을 선택하여 새로운 객체에 저장하고 sub_data2.csv로 저장하시오.(구분을 comma 사용)
titanic2 = raw_data[31:100,seq(2,10,2)]
write.csv(titanic2,file='sub_data2.csv')
#17. raw_data에서 결측값의 갯수를 구하시오.
sum(is.na(raw_data))
#18. raw_data에서 결측값의 위치를 1차원 인덱스로 찾으시오.
which(is.na(raw_data))
#19. raw_data에서 결측값의 위치를 2차원 인덱스로 찾으시오.
which(is.na(raw_data),T)
#20. raw_data의 Age변수의 결측값의 위치를 index 변수에 저장하고 이를 이용하여 모든 결측 값을 20으로 변경하시오.
index <- list(which(is.na(raw_data),T)[,1])
raw_data[index[[1]],6]=20
#21. If 조건문을 활용하여, raw_data의 Age 변수를 활용하여 10이상 20미만, 20이상 30미만 … 60이상 70미만, 그 외로출력하는 r프로그램을 작성하시오.
age <- raw_data[,6]
for(i in age){
if(i>=70){
  cat("\n 그 외")
}else if(i>=60){
  cat('\n 60이상 70미만')
}else if(i>=50){
  cat('\n 50이상 60미만')
}else if(i>=40){
  cat('\n 40이상 50미만')
}else if(i>=30){
  cat('\n 30이상 40미만')
}else if(i>=20){
  cat('\n 20이상 30미만')
}else if(i>=10){
  cat('\n 10이상 20미만')
}else{
  cat('\n 그 외')
}}
#22. If 조건문을 활용하여 raw_data의 Cabin 변수에서 결측값이 들어간 위치에 ‘DELETE’라는 값으로 변경하시오.
raw_data[raw_data['Cabin'] == '', 'Cabin'] = 'DELETE'
raw_data['Cabin'][1]
