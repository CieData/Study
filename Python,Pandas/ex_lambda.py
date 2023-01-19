# ----------------------------------------------------------
# 람다 함수 : 익명함수, 1줄 함수
# 짧은코드
# 문법 형식 lambda 인자 : 실행코드
# ----------------------------------------------------------
# 입력 받은 숫자를 모두 더해서 합계 출력하는 코드
nums=input('원하는 수 만큼 숫자를 입력하세요. (예시 : 1 3 4 ...)')
nums=nums.split() #['1','3','4',...]
#1
for i in range(len(nums)):
    nums[i]=int(nums[i])
#2(리스트 컴프리핸션)
nums1=[int(i) for i in nums]
#3(내장함수) => map(함수명, 반복가능객체) -> map 객체
nums2=list(map(int,nums))

def t(num):
    return num*3
nums3=list(map(t,nums))
nums4=list(map(lambda x : x*4,nums))

print(nums1,nums2,nums3,nums4)