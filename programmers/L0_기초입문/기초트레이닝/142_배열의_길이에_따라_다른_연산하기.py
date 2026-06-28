# 배열의 길이에 따라 다른 연산하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181854
# 알고리즘: 함수(메서드)
# 작성자: 백하은
# 작성일: 2026. 06. 28. 18:47:02

def solution(arr, n):
    arr_length = len(arr)
    
    # 배열의 길이가 짝수 -> 짝수 인덱스에 존재하는 숫자에 +n
    if arr_length % 2 == 0:
        for i in range(1,arr_length,2):
            arr[i] = arr[i] + n
    else:
        for i in range(0,arr_length,2):
            arr[i] = arr[i] + n
            
    return arr