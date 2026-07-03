# 배열 만들기 1
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181901
# 알고리즘: 리스트(배열)
# 작성자: 백하은
# 작성일: 2026. 07. 03. 15:38:47

def solution(n, k):
    answer = []
    
    for i in range(k, n+1, k):
        answer.append(i)
    
    return answer