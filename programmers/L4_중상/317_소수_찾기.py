# 소수 찾기
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42839
# 알고리즘: 완전탐색, 수학
# 작성자: 백하은
# 작성일: 2026. 07. 22. 21:56:38

# 순열
from itertools import permutations

# 소수를 판별하는 함수
# 1보다 큰 자연수 중에서 약수가 1과 자기 자신만 있는 수
def is_prime(n):
    if n < 2:
        return False
    
    # 2부터 n의 제곱근까지의 정수 중에서 나누어 떨어지는 수가 있는지 확인
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    
    return True


def solution(numbers):
    # numbers에 있는 숫자카드 조합으로 만들 수 있는 모든 숫자(중복 제외)
    all_nums = set()
    
    n = len(numbers)
    
    # 한 자릿수 ~ n 자릿수 숫자까지의 모든 순열 조합 제작
    for i in range(1, n+1):
        for m in permutations(numbers, i):
            num = int("".join(m))
            all_nums.add(num)
            
    # all_nums 중에서 소수의 개수 찾기
    answer = 0
    
    for x in all_nums:
        if is_prime(x):
            answer += 1
            
    # 최종 답
    return answer