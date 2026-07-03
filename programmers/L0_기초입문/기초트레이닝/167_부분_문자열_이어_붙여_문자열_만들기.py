# 부분 문자열 이어 붙여 문자열 만들기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181911
# 알고리즘: 문자열
# 작성자: 백하은
# 작성일: 2026. 07. 03. 15:41:14

def solution(my_strings, parts):
    answer = ''
    
    for idx in range(len(my_strings)):
        s,e = parts[idx]
        
        answer += my_strings[idx][s:e+1]
    
    return answer