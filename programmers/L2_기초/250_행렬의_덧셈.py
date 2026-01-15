# 행렬의 덧셈
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12950
# 알고리즘: 배열
# 작성자: 백하은
# 작성일: 2026. 01. 16. 01:55:48

def solution(arr1, arr2):
    answer = []
    # 행마다 반복
    for a in range(len(arr1)):
        row = []
        # 같은 행 내에서 열마다 반복
        for b in range(len(arr1[a])):
            row.append(arr1[a][b] + arr2[a][b])
        answer.append(row)
    return answer    