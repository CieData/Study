class addrh:
    #클래스 변수

    #생성자
    def __init__(self,name,phone,e_mail,group):
        self.name=name
        self.phone=phone
        self.e_mail=e_mail
        self.group=group
    
    #getter/setter

    #커스텀 메서드    
    def rephone(self,phone):
        self.phone=phone
    
    def remail(self, mail):
        self.mail=mail

    def regroup(self,group):
        self.group=group

    def delhuman(self):
        self.name=''
        self.phone=''
        self.e_mail=''
        self.group=''     
    
    def show(self):
        print(f'이름 : {self.name}\n번호 : {self.phone}\ne_mail : {self.e_mail}\n그룹 : {self.group}')
    
a=addrh('홍길동', '010-1234-5678','abcd1234@gmail.com','Friend')
a.show()


class bankh:
    #클래스 변수

    #생성자
    def __init__(self,name,phone,hnum,certificate,banknumber,password):
        self.name=name
        self.phone=phone
        self.__hnum=hnum
        self.__certificate=certificate
        self.banknumber=banknumber
        self.__password=password
    
    #getter/setter
    def get_hnum(self, hnum):
        return self.__hnum
    def get_certificate(self, certificate):
        return self.__certificate
    def set_password(self, password):
        self.__password=password

    #커스텀 메서드    
    def rephone(self,phone):
        self.phone=phone

    def delhuman(self):
        self.name=''
        self.phone=''
        self.__hnum=''
        self.__certificate=''
        self.banknumber=''
        self.__password=''  
    
    def show(self):
        print(f'이름 : {self.name}\n번호 : {self.phone}\n계좌번호 : {self.banknumber}')
a=bankh('홍길동', '010-1234-5678','000101-3151515','On','333-3333-3333-32',1234)
a.show()






























# # -----------------------------------------------------------
# # 주소록
# class address:
#     #클래스 변수

#     #생성자
#     def __init__(self):
#         self.human=[]
        
#     #getter/setter

#     #커스텀 메서드
#     def addhuman(self,name,phone,email,group):
#         self.human.append([name,phone,email,group])

#     def delhuman(self,name):
#         for i in range(len(self.human)):
#             if self.human[i][0]==name:
#                 self.human.remove(self.human[i])
#                 break
    
#     def rename(self,name,name2):
#         for i in range(len(self.human)):
#             if self.human[i][0]==name:
#                 self.human[i][0]=name2
#                 break        

#     def rephone(self,name,phone2):
#         for i in range(len(self.human)):
#             if self.human[i][0]==name:
#                 self.human[i][1]=phone2
#                 break

#     def reemail(self,name,email2):
#         for i in range(len(self.human)):
#             if self.human[i][0]==name:
#                 self.human[i][2]=email2
#                 break 

#     def regroup(self,name,group2):
#         for i in range(len(self.human)):
#             if self.human[i][0]==name:
#                 self.human[i][3]=group2
#                 break    

#     def show(self):
#         for i in range(len(self.human)):
#             print(self.human[i])





# # ----------------------------------------------
# # 은행
# class bankh:
#     #클래스 변수

#     #생성자
#     def __init__(self):
#         self.human=[]

#     #getter/setter

#     #커스텀 메서드 

#     def addhuman(self,name,phone,hnum,certificate,banknumber,password):
#         self.human.append([name,phone,hnum,certificate,banknumber,password])
    
#     def rephone(self,name,phone):
#         for i in range(len(self.human)):
#             if self.human[i][0]==name:
#                 self.human[i][1]=phone
#                 break
    
#     def recertificate(self,name,certificate):
#         for i in range(len(self.human)):
#             if self.human[i][0]==name:
#                 self.human[i][3]=certificate
#                 break
    
#     def repassword(self,name,password):
#         for i in range(len(self.human)):
#             if self.human[i][0]==name:
#                 self.human[i][5]=password
#                 break

#     def delhuman(self,name):
#         for i in range(len(self.human)):
#             if self.human[i][0]==name:
#                 self.human.remove(self.human[i])
#                 break    
    
#     def show(self):
#         for i in range(len(self.human)):
#             print(self.human[i])


