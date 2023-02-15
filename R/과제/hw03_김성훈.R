#1. for 문을 이용하여 구구단 1단부터 9단까지 출력하는 코드를 작성하시오.
for(i in 1:9){
  for(j in 1:9){
    cat(j,'*',i,'=',i*j,'\t')
  }
  cat('\n')
}
#2. 1번의 구구단 출력을 아래와 같이 진행하여 보시오 (탭이 안되시면 
for(i in 1:3){
  for(j in 1:9){
    for(k in seq(i,i+6,3)){
      cat(k,'*',j,'=',k*j,'\t')
    }
    cat('\n')
  }
}
#3. while 문과 조건문을 이용하여 아래와 같이 출력하는 코드를 작성하시오.
i=1
while(i<=5){
  if(i<3){
    cat(rep('*',i*2-1), rep(' ',4*(3-i)), rep('*',i*2-1),'\n')
  } else if(i==3){
    cat(rep('*',(5-i)*2+1), rep('*',i*2-1),'\n')
  } else {
    cat(rep('*',(5-i)*2+1), rep(' ',4*(i-3)), rep('*',(5-i)*2+1),'\n')
  }
  i = i +1
}
#4. 1에서 부터 100까지 차례로 더해 나갈 때, 처음으로 합이 1000을 넘게 만드는 수는 무엇인지 for문과 if문 그리고 break 문을 이용하여 구하여라. 또한 처음으로 1000을 넘었을 때, 누적합은 얼마인지 구하여라.
tot = 0
for(i in 1:100){
  tot = tot + i
  if(tot>1000){
    cat(tot)
    break
  }
}
#5. 반복문을 이용하여 50에서 100까지의 합을 계산할 때, 짝수의 합을 계 산하는 코드를 작성하시오.(단, next 함수를 써서 작성 하시오.)
tot = 0
for(i in 50:100){
  if(i%%2==1){next}
  tot = tot + i
}
#6. 하나의 벡터를 입력 받아 벡터의 길이, 원소의 합, 최솟값, 최댓값, 평균, 분산을 반환하는 함수를작성하고 x = 1:10에 대한 결과 를 확인하시오.
x <- 1:10
vec_info <-  function(x){
  l = c(length(x), sum(x), min(x), max(x), mean(x), var(x))
  return(l)
}
vec_info(x)
#7. 6에서 작성한 함수에 새로운 인수를 추가하여 1인 경우 벡터의 길이, 2 인 경우 원소의 합과 같이 특정 값을선택할 수 있도록 함수를 수정하 시오. x=1:10의 값을 이용하여 각각의 경우에 대해서 결과를 확인하시오.
x <- 1:10
vec_info1 <-  function(x,type){
  l = switch(type, length(x), sum(x), min(x), max(x), mean(x), var(x))
  return(l)
}
vec_info1(x,2)
#8. 7에서 작성한 함수에서 새로운 인수를 생략 시 원소의 합이 출력하도록 default 설정을 적용하시오.
x <- 1:10
vec_info2 <-  function(x,type = 2){
  l = switch(type, length(x), sum(x), min(x), max(x), mean(x), var(x))
  return(l)
}
vec_info2(x)
#9. 1 – 9 사이의 숫자 2개를 입력 받아 작은 수 부터 큰 수까지의 구구단을 출력하는 함수를 작성하시오.(ex, 3과 4를 입력 시)
googoo <- function(x,y){
  for(i in x:y){
    for(j in 1:9){
      cat(i,'*',j,'=',i*j,'\n')
    }
  }
}
googoo(1,5)
min(3,5)
