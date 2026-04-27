from func import *

# 변수 내용은 달라도 됩니다.
meet_day = "수요일"
hard_day = "목요일"
taste = "매콤해"
your_gender = "여자"
my_gender = "여자"
your_feelings = "칭찬해"
busy_reasons = {
    "월요일": "소교 수업 듣지",
    "화요일": "프언특 수업 들어",
    "수요일": "어정쩡한",
    "목요일": "바빠",
    "금요일": "필라테스 가야할 것 같은",
    "토요일": "휴식이 필요해",
    "일요일": None,
}

'''INTRO'''
intro(busy_reasons, meet_day, hard_day)
print()

'''1절'''
print_chorus(meet_day) 
print()
print_mind_control(hard_day)
print()
print_every_second(taste, your_gender)
print()

'''2절'''
print_chorus(meet_day) 
print()

print("딱히 보고 싶은 영화는 없지만")
print("딱히 먹고 싶은 메뉴는 없지만")
print()

print_mind_control(hard_day) # 수정
print_every_second(taste, your_gender) # 수정
print()

'''OUTRO'''
print_outro(my_gender, your_feelings, meet_day)
print()