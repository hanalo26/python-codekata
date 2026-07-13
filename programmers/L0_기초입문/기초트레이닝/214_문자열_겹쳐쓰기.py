# 문자열 겹쳐쓰기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181943
# 알고리즘: 연산
# 작성자: 백하은
# 작성일: 2026. 07. 13. 11:45:48

def solution(my_string, overwrite_string, s):
    front = my_string[:s]
    
    # 덮어 써지지 않는 글자의 인덱스
    end_idx = s + len(overwrite_string)
    
    back = my_string[end_idx:]
    
    
    return front + overwrite_string + back