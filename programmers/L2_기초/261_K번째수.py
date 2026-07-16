# K번째수
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42748
# 알고리즘: 정렬
# 작성자: 백하은
# 작성일: 2026. 07. 16. 12:12:08

def solution(array, commands):
    answer = []
    
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        
        sliced_list = array[i-1:j]
        
        sorted_list = sorted(sliced_list)
        
        answer.append(sorted_list[k-1])
    
    return answer