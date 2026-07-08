# 문자열 뒤집기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181905
# 알고리즘: 문자열
# 작성자: 백하은
# 작성일: 2026. 07. 08. 14:07:20

def solution(my_string, s, e):
    answer = my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
    return answer