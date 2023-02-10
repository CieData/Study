getwd()

x <- vector()
for(i in 1:5){
  x[i] <- i
}

x <- 3
for(i in 1:9){
  cat(x,'*',i,'=',x*i,'\n')
}

for(i in 1:5){
  cat(rep('*',i),'\n')
}

x <- c(1,2,3,4,5)
y <- 0
for(i in x){
  y <- y + (i / length(x))
}


y <- 0
cnt <- 0
for(i in x){
  if(i%%2==1){
    y <- y + i
    cnt <- cnt + 1
  }
}
y/cnt



xmat <- matrix(NA,4,5)
xmat
for(i in 1:4){
  for(j in 1:5){
    xmat[i,j] <- i + (4*(j-1))
  }
}



i = 1
while(i<=5){
  cat(rep('*',i),'\n')
  i = i+1
}


s=0
for(i in 1:10){
  if(i%%2==1){next}
  s = s+1
}


x <- c(1,5,2,3,8)
y <- 0
cnt <- 0
for(i in x){
  if(i%%2==1){next}
  y <- y + i
  cnt <- cnt + 1
}
y/cnt




####