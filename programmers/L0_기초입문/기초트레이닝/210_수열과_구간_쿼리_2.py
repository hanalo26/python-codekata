# 수열과 구간 쿼리 2
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181923
# 알고리즘: 반복문
# 작성자: 백하은
# 작성일: 2026. 07. 12. 16:35:47

def solution(arr, queries):
    answer = []
    
    for s,e,k in queries:
        # k보다 큰 값을 담을 리스트
        candidate = []
        
        for i in range(s,e+1):
            if arr[i] > k:
                candidate.append(arr[i])
        
        if candidate: # 리스트가 비어있다면 실행되지 않음
            answer.append(min(candidate))
        else:          # 리스트가 비어있을 때, 실행됨
            answer.append(-1)

    return answer