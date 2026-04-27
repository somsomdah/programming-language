from func import *

# [TODO] 전역변수 정의하기: 자유롭게 정해 보세요
meet_day = "수요일" # 우~ 이번 주 {meet_day}
hard_day = "목요일" # {hard_day}까지 기다리긴 힘들어
taste = "새콤해" # 일분 일초가 {taste}해
your_gender = "여자" # 이 {your_gender} 도대체 뭐야
my_gender = "여자" # 이 {my_gender} 도대체 뭐야
your_feelings = "사랑해" # {your_feelings}주지 않고는 못 배기겠어

# [참고] busy_resons: get_intro 함수의 인자로 사용되는 딕셔너리
# [TODO] 자유롭게 수정해 보세요
busy_reasons = {
    "월요일": "바쁘지", # 예) "일이 너무 먾지", "피곤하지", "바쁘지"
    "화요일": "", # 예) "프언 수업듣지", "운동하러 가지", "친구 만나기로 했지"
    "수요일": "",
    "목요일": "",
    "금요일": "",
    "토요일": "",
    "일요일": "",
}

# [TODO] 변수에 func.py에서 정의한 함수를 호출하여 반환값 저장하기
intro_line = get_intro(busy_reasons, meet_day, hard_day)
print_chorus_line = ""
mind_control_line = ""
every_second_line = ""
outro_line = ""

# [주의] AI 프롬프트로 변환하기 위한 코드입니다. 수정 금지!!
def build_prompt():
    singer1 = "Female" if (my_gender == "여자") else "Male"
    singer2 = "Female" if (your_gender == "여자") else "Male"
    
    chorus = f"[chorus: {singer1} and {singer2} Both in Unison]\n{print_chorus_line}" if (my_gender != your_gender)\
    else f"[chorus: two different {singer1}s Both in Unison]\n{print_chorus_line}"
        
    post_chorus_1 = f"[Post-chorus 1: {singer1} Solo]\n{mind_control_line}"
    post_chorus_2 = f"[Post-chorus 2: {singer1} Solo]\n{every_second_line}"
    
    intro = f"[Intro: {singer1} Solo]\n{intro_line}"
    outro = f"[Outro: {singer2} Solo]\n{outro_line}"
    
    bridge = f"[Bridge: {singer2} Solo]\n딱히 보고 싶은 영화는 없지만\n딱히 먹고 싶은 메뉴는 없지만"
    switch_voice = f"[SWITCH TO {singer2} VOCAL]" if (my_gender != your_gender) else f"[SWITCH TO a Different {singer2} VOCAL]"
    return f"""\
{intro}

{chorus}

{post_chorus_1}
        
{post_chorus_2}

[Breath]

{chorus}

{bridge}

{post_chorus_1}

{post_chorus_2}

[Breath]

{switch_voice}

{outro}\
"""
         