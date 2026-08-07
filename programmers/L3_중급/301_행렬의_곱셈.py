# 행렬의 곱셈
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12949
# 알고리즘: 배열
# 작성자: 백하은
# 작성일: 2026. 08. 07. 18:46:35

def solution(arr1, arr2):
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = len(arr2), len(arr2[0])
    
    answer = [[0]*c2 for _ in range(r1)]
    
    # 행렬 곱셈 수행
    for i in range(r1):          # arr1의 행
        for j in range(c2):      # arr2의 열
            for k in range(c1):  # 공통 길이 (arr1의 열 = arr2의 행)
                answer[i][j] += arr1[i][k] * arr2[k][j]
    
    return answer