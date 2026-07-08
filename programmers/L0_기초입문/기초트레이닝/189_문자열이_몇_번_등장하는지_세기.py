# 문자열이 몇 번 등장하는지 세기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181871
# 알고리즘: 문자열
# 작성자: 백하은
# 작성일: 2026. 07. 08. 14:26:09

def solution(myString, pat):
    answer = 0
    
    # pat의 길이만큼 잘라야 하므로, 인덱스 범위를 초과하지 않도록 제한
    for i in range(len(myString)-len(pat)+1):
        if myString[i:i+len(pat)] == pat:
            answer += 1
    
    return answer