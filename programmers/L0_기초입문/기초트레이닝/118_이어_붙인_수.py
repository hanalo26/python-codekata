# 이어 붙인 수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181928
# 알고리즘: 조건문
# 작성자: 백하은
# 작성일: 2026. 06. 20. 13:17:29

def solution(num_list):
    answer_1 = "" #짝수
    answer_2 = "" #홀수
    
    for i in num_list:
        if i % 2 == 0:
            answer_1 += str(i)
        else:
            answer_2 += str(i)
    
    return int(answer_1) + int(answer_2)