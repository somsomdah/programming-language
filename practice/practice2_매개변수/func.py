## [나쁜 예시] 비슷한 기능을 하는 함수를 여러 개 만듦

def print_chorus_meet_friday():
    print("우~ 이번 주 금요일")
    print("우~ 금요일에 시간 어때요")
    
def print_chorus_meet_wednesday():
    print("우~ 이번 주 수요일") # 금요일 -> 수요일
    print("우~ 수요일에 시간 어때요")
    
def print_mind_control_weekend():
    print("주말까지 기다리긴 힘들어")
    print("시간아 달려라 시계를 더 보채고 싶지만 (mind control)")
    
def print_mind_control_thursday():
    print("목요일까지 기다리긴 힘들어") # 주말 -> 목요일
    print("시간아 달려라 시계를 더 보채고 싶지만 (mind control)")

def print_every_second_sweet():
    print("일분 일초가 달콤해")
    print("이 남자 도대체 뭐야")
    print("사랑에 빠지지 않곤 못 배기겠어")
    print("온 종일 내 맘은 저기 시계바늘 위에 올라타")
    print("한 칸씩 그대에게 더 가까이")
    
def print_every_second_spicy():
    print("일분 일초가 매콤해") # 달콤해 -> 매콤해
    print("이 여자 도대체 뭐야") # 남자 -> 여자
    print("사랑에 빠지지 않곤 못 배기겠어")
    print("온 종일 내 맘은 저기 시계바늘 위에 올라타")
    print("한 칸씩 그대에게 더 가까이") 
    print()

    
# [TODO] 매개변수를 활용하여 함수 하나로 통합하기

# 노래의 코러스(하이라이트)를 출력하는 함수
def print_chorus(meet_day): 
    print(f"우~ 이번 주 {meet_day}")
    print(f"우~ {meet_day}에 시간 어때요")

# [TODO] 매개변수를 활용하여 개선하기
def print_mind_control(hard_day):
    pass

# [TODO] 매개변수를 활용하여 개선하기
def print_every_second(taste, gender):
    pass
    