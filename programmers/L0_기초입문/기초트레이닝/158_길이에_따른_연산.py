# 길이에 따른 연산
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181879
# 알고리즘: 리스트(배열)
# 작성자: 백하은
# 작성일: 2026. 01. 16. 02:04:32

def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        answer = 1
        for i in num_list:
            answer = answer*i
        return answer    