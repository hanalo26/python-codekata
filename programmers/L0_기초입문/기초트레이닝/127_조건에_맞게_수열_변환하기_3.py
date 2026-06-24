# 조건에 맞게 수열 변환하기 3
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181835
# 알고리즘: 반복문 활용
# 작성자: 백하은
# 작성일: 2026. 06. 24. 21:34:46

def solution(arr, k):
    answer = []
    
    if k % 2 != 0:
        for i in arr:
            n = k * i
            answer.append(n)
    else:
        for i in arr:
            m = i + k
            answer.append(m)
            
    return answer