# 정수 내림차순으로 배치하기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12933
# 알고리즘: 문자열, 정렬
# 작성자: 백하은
# 작성일: 2026. 01. 16. 01:48:42

def solution(n):
    n_str=str(n)
    n_list=list(n_str)
    n_list.sort(reverse=True) #내림차순 정렬
    
    result_str=""
    
    for i in n_list:
        result_str = result_str+i  
    
    return int(result_str)