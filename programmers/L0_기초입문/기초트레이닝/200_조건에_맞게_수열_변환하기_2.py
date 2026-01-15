# 조건에 맞게 수열 변환하기 2
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181881
# 알고리즘: 리스트(배열)
# 작성자: 백하은
# 작성일: 2026. 01. 16. 02:05:01

def solution(arr):
    answer = 0
    
    while True:
        changed_arr = False
        new_arr = arr[:]
        
        for i in range(len(arr)):
            element = arr[i]
            
            if element >= 50 and element % 2 == 0:
                new_element = element // 2
            elif element < 50 and element % 2 == 1:
                new_element = 2 * element + 1
            else:
                new_element = element
            
            if new_element != element:
                changed_arr = True
            
            new_arr[i] = new_element
            
        if not changed_arr:
            return answer
            
        arr = new_arr
        answer += 1
                
                