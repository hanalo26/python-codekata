# 배열 만들기 5
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181912
# 알고리즘: 문자열
# 작성자: 백하은
# 작성일: 2026. 07. 07. 16:31:14

def solution(intStrs, k, s, l):
    answer = []
    
    # intStrs의 원소를 하나씩 꺼내
    # 각 원소별로 s번 인덱스부터 l만큼의 글자를 슬라이싱
    for str in intStrs:
        str_int = str[s:s+l]
        
        # 숫자로 변환
        num = int(str_int)
        
        # k보다 큰 것만 answer에 추가
        if num > k:
            answer.append(num)
    
    return answer