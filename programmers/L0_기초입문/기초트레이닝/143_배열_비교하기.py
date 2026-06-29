# 배열 비교하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181856
# 알고리즘: 함수(메서드)
# 작성자: 백하은
# 작성일: 2026. 06. 29. 16:12:53

def solution(arr1, arr2):
    if len(arr1) > len(arr2):
        return 1
    
    elif len(arr1) < len(arr2):
        return -1
    
    else:
        sum_of_arr1 = 0
        sum_of_arr2 = 0
        
        for a in arr1:
            sum_of_arr1 += int(a)
        for b in arr2:
            sum_of_arr2 += int(b)
            
        if sum_of_arr1 > sum_of_arr2:
            return 1
        elif sum_of_arr1 < sum_of_arr2:
            return -1
        else:
            return 0