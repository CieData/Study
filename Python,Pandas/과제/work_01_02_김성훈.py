import random as r
import pandas as pd

# 1
data1=[r.randint(1,101) for i in range(30)]
sr1=pd.Series(data1)
sr1

#2-1
data2=set()
while len(data2)!=30:
    data2.add(r.randint(1,101))
data2=list(data2)
sr2=pd.Series(data2)
sr2

#2-2
data2_1=[]
while len(data2_1)!=30:
    n=r.randint(1,101)
    if n not in data2_1:
        data2_1.append(n)
sr2_1=pd.Series(data2_1)
sr2_1

#3
data3=[r.random() for i in range(10)]
sr3=pd.Series(data3)
sr3