# 특별한 이차원 배열 2
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181831
# 알고리즘: 이차원 리스트(배열)
# 작성자: 백하은
# 작성일: 2026. 07. 06. 14:27:51

def solution(arr):
    n = len(arr)
    
    for i in range(n):
        # 이중검사를 피하기 위해 j의 범위를 i 이상으로 제한
        for j in range(i,n):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1