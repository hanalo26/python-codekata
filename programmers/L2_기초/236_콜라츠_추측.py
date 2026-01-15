# 콜라츠 추측
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12943
# 알고리즘: 시뮬레이션, 반복문
# 작성자: 백하은
# 작성일: 2026. 01. 16. 01:50:44

def solution(num):
    count = 0
    
    if num == 1:
        return 0
    else:
        while num != 1 and count < 500:
            if num % 2 == 0:
                num = num // 2
            else:
                num = num * 3 + 1
            
            count += 1
            
        return count if num == 1 else -1
    