# 잘라서 배열로 저장하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120913
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 04. 05. 00:30:35

def solution(my_str, n):
    answer = []
    
    for i in range(0,len(my_str), n):
        # i부터 i + n까지 문자열을 잘라서 리스트에 추가
        answer.append(my_str[i:i+n])
    
    return answer