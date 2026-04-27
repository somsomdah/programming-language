def print_chorus(meet_day):
    print(f"우~ 이번 주 {meet_day}")
    print(f"우~ {meet_day}에 시간 어때요")
    
def print_mind_control(hard_day):
    print(f"{hard_day}까지 기다리긴 힘들어")
    print("시간아 달려라 시계를 더 보채고 싶지만 (mind control)")

def print_every_second(taste, your_gender):
    print(f"일분 일초가 {taste}")
    print(f"이 {your_gender} 도대체 뭐야")
    print("사랑에 빠지지 않곤 못 배기겠어")
    print("온 종일 내 맘은 저기 시계바늘 위에 올라타")
    print("한 칸씩 그대에게 더 가까이")
 
def intro(busy_reasons, meet_day, hard_day):
  deco = [("엔 아마", "않을까"), ("도", "안 그래"), ("은 뭔가", "느낌"), ("은 그냥 내가 왠지", "")]
  deco_idx = 0
  
  for day in busy_reasons:
    if day == meet_day or day == hard_day:
      continue
    reason = busy_reasons[day]
    if reason:
      print(f"{day}{deco[deco_idx][0]} {reason} {deco[deco_idx][1]}")
      deco_idx = (deco_idx + 1) % len(deco) 

def print_outro(my_gender, your_feelings, meet_day):
    print("나 뭔가에 홀린 것 같아")
    print(f"이 {my_gender} 도대체 뭐야")
    print(f"{your_feelings}주지 않고는 못 배기겠어")
    print(f"돌아오는 이번 주 {meet_day}에 만나요")
    print("그 날 내 맘을 더 가져가줘요")

