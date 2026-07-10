# 수열과 구간 쿼리 4
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181922
# 알고리즘: 반복문
# 작성자: 백하은
# 작성일: 2026. 07. 10. 22:06:06

def solution(arr, queries):
    # s: 시작
    # e: 끝
    # k: 배수 기준
    for s,e,k in queries:
        for i in range(s,e+1):
            if i % k == 0:
                arr[i] += 1
                
    return arr