# 꼬리 문자열
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181841
# 알고리즘: 조건문 활용
# 작성자: 백하은
# 작성일: 2026. 06. 26. 11:54:45

def solution(str_list, ex):
    answer = ''
    
    for str in str_list:
        if ex not in str:
            answer += str
    
    return answer