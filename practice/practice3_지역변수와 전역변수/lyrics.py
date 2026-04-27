from func import *

## [나쁜 예시] 같은 값을 반복해서 입력함.

# [TODO] 전역변수 선언하기
# 변수 내용은 자유롭게 적어주세요.
meet_day = "" # 만나고 싶은 요일
hard_day = "" # 기다리기 힘든 요일
taste = "" # 일분 일초가 {taste}해
your_gender = "" # 상대방의 성별
my_gender = "" # 나의 성별
your_feelings = "" # {your_feelings}주지 않고는 못 배기겠어
busy_reasons = {
    "월요일": "",
    "화요일": "",
    "수요일": "",
    "목요일": "",
    "금요일": "",
    "토요일": "",
    "일요일": "",
}

'''INTRO'''
print_intro(busy_reasons, meet_day, hard_day)
print()

'''1절'''
# [TODO] 전역 변수를 사용하여 함수 재구성하기
print_chorus("수요일")   
print()       
print_mind_control("목요일") 
print()
print_every_second("매콤해", "여자")
print()

'''2절'''
# [TODO] 전역 변수를 사용하여 함수 재구성하기
print_chorus("수요일")   
print() 

print("딱히 보고 싶은 영화는 없지만")
print("딱히 먹고 싶은 메뉴는 없지만")
print()

# [TODO] 전역 변수를 사용하여 함수 재구성하기
print_mind_control("목요일") 
print()
print_every_second("매콤해", "여자") 
print()


'''OUTRO'''
# [TODO] 전역 변수를 사용하여 함수 재구성하기
print_outro("여자", "칭찬해", "수요일")