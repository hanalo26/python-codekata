# 문자열 여러 번 뒤집기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181913
# 알고리즘: 문자열
# 작성자: 백하은
# 작성일: 2026. 07. 12. 16:24:53

def solution(my_string, queries):
    # 문자열을 리스트로 변환
    str_list = list(my_string)
    
    # 쿼리를 하나씩 꺼낸 뒤, 해당 부분 뒤집기
    for s,e in queries:
        str_list[s:e+1] = str_list[s:e+1][::-1]
        
    # 리스트를 문자열로 변환
    return "".join(str_list)