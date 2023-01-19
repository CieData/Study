# ----------------------------------------------------------
# 계산기
# ----------------------------------------------------------
class calc:
    def __init__(self,file_name):
        self.file_name=file_name

    def number(self,operator,num):
        fp=open(self.file_name,mode='a',encoding='utf-8')
        if operator=='+':
            fp.write(f'{self.num}{operator}{num}=')
            self.num+=num
            fp.write(f'{self.num}\n')
            fp.close()
        elif operator=='-':
            fp.write(f'{self.num}{operator}{num}=')
            self.num-=num
            fp.write(f'{self.num}\n')
            fp.close()
        elif operator=='*':
            fp.write(f'{self.num}{operator}{num}=')
            self.num*=num
            fp.write(f'{self.num}\n')
            fp.close()
        elif operator=='/' or operator=='//' or operator=='%':
            if num==0:
                print('0을 나누려고 합니다. 다시 입력해주세요 : ')
            else:
                if operator=='/':
                    fp.write(f'{self.num}{operator}{num}=')
                    self.num/=num
                    fp.write(f'{self.num}\n')
                    fp.close()
                elif operator=='//':
                    fp.write(f'{self.num}{operator}{num}=')
                    self.num//=num
                    fp.write(f'{self.num}\n')
                    fp.close()
                else:
                    fp.write(f'{self.num}{operator}{num}=')
                    self.num%=num
                    fp.write(f'{self.num}\n')
                    fp.close()
        elif operator=='**':
            fp.write(f'{self.num}{operator}2=')
            self.num**=2
            fp.write(f'{self.num}\n')
            fp.close()
        elif operator=='root':
            fp.write(f'{self.num}**(1/2)=')
            self.num**=(1/2)
            fp.write(f'{self.num}\n')
            fp.close()

    def ww(self):
        self.num=0
        while True:
            oper=input('연산자 : ')
            if oper=='=':
                break
            if oper=='**' or oper=='root':
                self.number(oper,0)
            else:
                n=float(input('숫자   : ')) 
                self.number(oper,n)
        
a=calc('과제\history.txt')
a.ww()
