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
a <- c(1,3,5,6)
std.ftn <- function(x){
  return(list(mean=mean(x),var=var(x)))
}
l <- std.ftn(a) 
l$mean


a <- c(1,3,5)
noact <- function(x,type=1){
  if(type==1){a[1] <- 3}
  if(type==2){a[1] <<- 3}
  return(a)
}
noact(10)
a
noact(5,2)
a


install.packages("ggplot2") 
library(ggplot2)
par("mar")

par(mar=c(1,1,1,1))

draw_koch_snowflake <- function(order, x, y, len, angle) {
  if (order == 0) {
    x2 <- x + len * cos(angle)
    y2 <- y + len * sin(angle)
    plot(c(x, x2), c(y, y2))
    
    draw_koch_snowflake(order - 1, x2, y2, len * 0.8, angle - 30)
    draw_koch_snowflake(order - 1, x2, y2, len * 0.8, angle - 30)
  }
  else {
    len <- len / 3
    draw_koch_snowflake(order - 1, x, y, len, angle)
    x <- x + len * cos(angle)
    y <- y + len * sin(angle)
    angle <- angle + pi / 3
    draw_koch_snowflake(order - 1, x, y, len, angle)
    x <- x + len * cos(angle)
    y <- y + len * sin(angle)
    angle <- angle - 2 * pi / 3
    draw_koch_snowflake(order - 1, x, y, len, angle)
    x <- x + len * cos(angle)
  }
}
draw_koch_snowflake(12,100,100,70,90)
