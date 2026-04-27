from func import *

# [TODO] 전역변수 정의하기: 적절히 수정해 보세요
meet_day = ""
hard_day = ""
taste = ""
your_gender = "" # 예) "남자", "여자"
my_gender = "" # 예) "남자", "여자"
your_feelings = "" # 예) "좋아", "싫어", "모르겠어"

# [참고] 아래 busy_reasons 딕셔너리는 get_intro 함수의 인자로 사용됩니다.
busy_reasons = {
    "월요일": "바쁘지", # 예) "일이 너무 먾지", "피곤하지", "바쁘지"
    "화요일": "", # 예) "프언 수업듣지", "운동하러 가지", "친구 만나기로 했지"
    "수요일": "",
    "목요일": "",
    "금요일": "",
    "토요일": "",
    "일요일": "",
}

# [TODO] 변수에 func.py에서 정의한 함수를 호출하여 값을 할당하기
intro_line = get_intro(busy_reasons, meet_day, hard_day)
print_chorus_line = ""
mind_control_line = ""
every_second_line = ""
outro_line = ""


'''INTRO'''
print(intro_line)

'''1절'''
print(print_chorus_line)

# [TODO] print문과 전역 변수를 활용하여 수정하기
# print_mind_control(meet_day) 
# print_every_second(taste, your_gender) 

'''2절'''
print(print_chorus_line)

print("딱히 보고 싶은 영화는 없지만")
print("딱히 먹고 싶은 메뉴는 없지만")
print()

# [TODO] print문과 전역 변수를 활용하여 수정하기
# print_mind_control(meet_day) 
# print_every_second(taste, your_gender) 

'''OUTRO'''
print(outro_line)


# [주의] 아래 코드는 AI 프롬프트로 변환하기 위한 코드입니다. 실습과는 무관하니 수정하지 말아주세요.
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
         