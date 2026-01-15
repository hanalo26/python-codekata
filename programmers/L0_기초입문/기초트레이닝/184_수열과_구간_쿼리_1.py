# 수열과 구간 쿼리 1
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181883
# 알고리즘: 리스트(배열)
# 작성자: 백하은
# 작성일: 2026. 01. 16. 02:05:32

def solution(arr, queries):
    n = len(arr)
    
    diff_arr = [0] * (n+1)
    
    # queries는 [s,e]의 형태로 어떤 구간에 +1을 해야 하는지에 관한 정보가 있음
    for s, e in queries:
        diff_arr[s] += 1
        diff_arr[e+1] -= 1
        
    add_total = 0
    for i in range(n):
        add_total += diff_arr[i]
        arr[i] += add_total # 누적합을 계산하고, 실제 arr에 반영
        
    return arr    