# 문자열 섞기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181942
# 알고리즘: 연산
# 작성자: 백하은
# 작성일: 2026. 07. 06. 15:38:03

def solution(str1, str2):
    answer = ''
    
    for i in range(len(str1)):
        answer += str1[i]
        answer += str2[i]
    
    return answer