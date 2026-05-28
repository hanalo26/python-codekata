# 다항식 더하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120863
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 05. 28. 20:11:07

def solution(polynomial):
    parts = polynomial.split(' + ')
    x_sum = 0 # 일차항 계수의 합
    num_sum = 0 # 상수항의 합
    
    for part in parts:
        if 'x' in part:
            # 계수가 1인 경우와 2이상인 경우로 분리
            if part == 'x':
                x_sum += 1
            else:
                x_sum += int(part.replace('x', ''))
        else:
            num_sum += int(part)
    result = []
    
    if x_sum != 0:
        if x_sum == 1:
            result.append("x")
        else:
            result.append(f"{x_sum}x")
            
    # 상수항 정리
    if num_sum != 0:
        result.append(str(num_sum))
        
    return " + ".join(result)