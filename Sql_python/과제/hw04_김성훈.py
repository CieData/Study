import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
f_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=f_path).get_name()
rc('font', family=font_name)

FILE_NAME='C:\\Users\\hoon3\\SH_Git\\Study\\Sql_python\\과제\\'+input('Input file name : ')

fp=open(FILE_NAME,mode='r',encoding='utf-8')
allData=fp.read()
fp.close()
allData
a='abcdefghijklmnopqrstuvwxyz'
large={}
small={}
for i in a:
    large[i.upper()]=0
    small[i]=0
for i in allData:
    if i.isalpha():
        if i.islower():
            small[i]+=1
        else:
            large[i]+=1
small=dict(sorted(small.items(),key=lambda x : -x[1]))
large=dict(sorted(large.items(),key=lambda x : -x[1]))

for i in range(26):
    if small[a[i]]==0:
        del small[a[i]]
    if large[a[i].upper()]==0:
        del large[a[i].upper()]
print(f'대문자 :\n{large}\n소문자 :\n{small}\n')

fig=plt.figure(figsize=(20,10))
ax1=fig.add_subplot(1,2,1)
ax2=fig.add_subplot(1,2,2)
ax1.set_title('대문자 개수')
ax2.set_title('소문자 개수')
ax1.set_xlabel('alphabet')
ax2.set_xlabel('alphabet')
ax1.set_ylabel('count')
ax2.set_ylabel('count')
fig.suptitle(f'알파벳 카운트 : {FILE_NAME[:-4]}')
# fig.tight_layout()
ax1.bar(large.keys(),large.values())
ax2.bar(small.keys(),small.values())