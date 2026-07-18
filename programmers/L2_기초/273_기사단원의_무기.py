# 기사단원의 무기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/136798
# 알고리즘: 수학
# 작성자: 백하은
# 작성일: 2026. 07. 18. 15:22:27

def cnt_divisor(n):
    cnt = 0
    
    # 1 ~ n의 제곱근까지 확인
    # 약수는 항상 pair로 존재하기 때문에, 제곱근 이후는 pair임
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            cnt += 1 # 약수이므로 카운트함
            if i * i != n: # 제곱근이 아닌 경우
                cnt += 1 # 약수이므로 카운트함
    return cnt

def solution(number, limit, power):
    total_iron = 0
    
    # 1 ~ number번 기사까지 확인
    for i in range(1,number+1):
        div_cnt = cnt_divisor(i)
        
        # 약수의 개수가 limit을 초과하면 지정된 power를 더함
        # limit을 초과하지 않으면 약수의 개수를 더함 
        if div_cnt > limit:
            total_iron += power
        else:
            total_iron += div_cnt
            
    return total_iron