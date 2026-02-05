# 인덱스 바꾸기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120895
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 02. 05. 09:38:54

def solution(my_string, num1, num2):
    my_string_list = []
    
    for i in my_string:
        my_string_list.append(i)
        
    temp =  my_string_list[num1]   
    
    my_string_list[num1] = my_string_list[num2]
    my_string_list[num2] = temp
    
    return "".join(my_string_list)