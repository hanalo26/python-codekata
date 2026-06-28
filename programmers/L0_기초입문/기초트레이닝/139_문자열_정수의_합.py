# 문자열 정수의 합
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181849
# 알고리즘: 함수(메서드)
# 작성자: 백하은
# 작성일: 2026. 06. 28. 18:39:25

def solution(num_str):
    answer = 0
    
    for i in num_str:
        answer += int(i)
        
    return answer