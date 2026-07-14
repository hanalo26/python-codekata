# 배열 조각하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181893
# 알고리즘: 리스트(배열)
# 작성자: 백하은
# 작성일: 2026. 07. 14. 10:45:47

def solution(arr, query):
    for i, q in enumerate(query):
        # 짝수 번째 쿼리일 때
        if i % 2 == 0:
            arr = arr[:q+1]
        
        # 홀수 번째 쿼리일 때
        else:
            arr = arr[q:]
        
    return arr