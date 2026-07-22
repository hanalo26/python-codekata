# 소수 찾기
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42839
# 알고리즘: 완전탐색, 수학
# 작성자: 백하은
# 작성일: 2026. 07. 22. 23:57:30

from itertools import permutations

# 어떤 숫자 x가 소수(prime number)인지 아닌지 판단하는 함수
def is_prime(x):
    # 조건
    # (1) 2이상의 정수일 것
    if x < 2:
        return False
    # (2) 약수가 자기자신과 1뿐일 것
    for n in range(2,int(x**0.5)+1):
        if x % n == 0:
            return False
    
    return True

# numbers에서 소수의 개수를 반환하는 함수
def solution(numbers):
    nums = list(numbers)
    
    # numbers에 있는 요소로 만들 수 있는 모든 숫자(중복 제외)
    all_nums = set()
    
    # 사용할 수 있는 요소의 개수
    n = len(numbers)
    
    # 만드는 숫자의 자릿수
    for i in range(1,n+1):
        # 순열 조합 시작!
        for m in permutations(nums,i):
            # 튜플 형태로 반환되기 때문에 int로 변환
            k = int("".join(m))
            all_nums.add(k)
            
    # all_nums에서 소수의 개수 count
    answer = 0
    
    for y in all_nums:
        if is_prime(y):
            answer += 1
            
    # 최종 답
    return answer