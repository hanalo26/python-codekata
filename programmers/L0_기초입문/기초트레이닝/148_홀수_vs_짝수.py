# 홀수 vs 짝수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181887
# 알고리즘: 리스트(배열)
# 작성자: 백하은
# 작성일: 2026. 06. 30. 13:46:46

def solution(num_list):
    
    # 홀수 번째 원소들의 합
    odd_nums = 0
    
    # 짝수 번째 원소들의 합
    even_nums = 0
    
    for i in range(0,len(num_list)):
        if (i+1) % 2 == 0:
            even_nums += num_list[i]
        else:
            odd_nums += num_list[i]
        
    return max(even_nums,odd_nums)