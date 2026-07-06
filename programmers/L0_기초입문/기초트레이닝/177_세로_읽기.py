# 세로 읽기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181904
# 알고리즘: 문자열
# 작성자: 백하은
# 작성일: 2026. 07. 06. 15:09:11

def solution(my_string, m, c):
    answer = ''
    
    # c-1 인덱스부터 시작해서 문자열 끝까지 m씩 더해가며 순회
    for i in range(c-1, len(my_string), m):
        answer += my_string[i]
        
    return answer