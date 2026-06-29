# x 사이의 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181867
# 알고리즘: 문자열
# 작성자: 백하은
# 작성일: 2026. 06. 29. 16:50:08

def solution(myString):
    answer = []
    
    # 'x'를 기준으로 문자열을 나눔
    for sub_str in myString.split('x'):
        answer.append(len(sub_str))
    
    return answer