# 크기가 작은 부분문자열
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/147355
# 알고리즘: 문자열
# 작성자: 백하은
# 작성일: 2026. 07. 15. 12:24:09

def solution(t, p):
    answer = 0
    len_t = len(t)
    len_p = len(p)
    p_num = int(p)
    
    for i in range(len_t-len_p+1):
        sub_str = t[i:i+len_p]
        
        # 잘라낸 부분문자열을 정수로 바꾸어 p와 비교
        if int(sub_str) <= p_num:
            answer += 1
    
    return answer