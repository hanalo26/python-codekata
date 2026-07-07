# 등차수열의 특정한 항만 더하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181931
# 알고리즘: 조건문
# 작성자: 백하은
# 작성일: 2026. 07. 07. 16:05:43

def solution(a, d, included):
    answer = 0
    
    for idx in range(len(included)):
        if included[idx]:
            answer += (a + idx*d)
    
    return answer