# 소수 찾기
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42839
# 알고리즘: 완전탐색, 수학
# 작성자: 백하은
# 작성일: 2026. 07. 24. 16:31:06

from itertools import permutations

# 소수(prime_number)인지 판단하는 함수
def is_prime(k):
    # 2보다 작은 정수라면 탈락
    if k < 2:
        return False
    
    # 1과 자기자신 외 다른 약수가 있다면 탈락
    for i in range(2, int(k**0.5)+1):
        if k % i == 0:
            return False
        
    # 모든 조건을 통과하면 소수 인정!
    return True

# 메인
def solution(numbers):
    # numbers에 담긴 숫자를 하나씩 꺼내서 순열조합 -> 숫자로 변환 -> 저장 -> 하나씩 꺼내서 is_prime() 함수에 넣어서 소수 판단
    # 소수로 판명날 때마다 +1씩 올라가는 변수 정의 후, return
    
    all_nums = set()
    
    n = len(numbers) # n자릿수의 숫자까지 모두 만들기 위해서
    
    for i in range(1,n+1): # 자릿수
        for m in permutations(numbers,i):
            num = int("".join(m))
            all_nums.add(num)
            
    # 소수의 개수
    cnt = 0
            
    for j in all_nums:
        if is_prime(j):
            cnt += 1
    
    return cnt