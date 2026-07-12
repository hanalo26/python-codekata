# 무작위로 K개의 수 뽑기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181858
# 알고리즘: 리스트(배열)
# 작성자: 백하은
# 작성일: 2026. 07. 12. 16:39:47

def solution(arr, k):
    answer = []
    
    for num in arr:
        if num in answer:
            continue
        else:
            answer.append(num)
        
        if len(answer) == k:
            return answer
        
    while len(answer) < k:
        answer.append(-1)
    
    return answer