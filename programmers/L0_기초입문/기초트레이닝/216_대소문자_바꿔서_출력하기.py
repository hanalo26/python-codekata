# 대소문자 바꿔서 출력하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181949
# 알고리즘: 출력
# 작성자: 백하은
# 작성일: 2026. 07. 13. 11:57:45

str = input()
answer = []

for txt in str:
    # 대문자 -> 소문자
    if txt.isupper():
        answer.append(txt.lower())
    
    # 소문자 -> 대문자
    else:
        answer.append(txt.upper())
        
    
print("".join(answer))