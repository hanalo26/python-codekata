# 문자열 묶기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181855
# 알고리즘: 함수(메서드)
# 작성자: 백하은
# 작성일: 2026. 07. 09. 15:45:37

def solution(strArr):
    # key: 문자열 길이
    # value: 해당 길이를 가진 문자열의 개수
    answer = {}
    
    for str in strArr:
        key = len(str)
        
        if key in answer:
            answer[key] += 1
        else:
            answer[key] = 1
    
    return max(answer.values())