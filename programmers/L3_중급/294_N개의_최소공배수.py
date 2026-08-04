# N개의 최소공배수
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12953
# 알고리즘: 수학
# 작성자: 백하은
# 작성일: 2026. 08. 04. 14:14:10

# 최소공배수를 구하는 메서드
from math import gcd


def solution(arr):
    answer = arr[0] # 최소공배수를 구하는 기준으로 설정
    
    # 앞에서부터 순회하면서 각 숫자끼리의 최소공배수를 계산하면서 최소 공배수 구하기
    # answer에 최소공배수 저장
    for n in arr[1:]:
        answer = (answer*n) // gcd(answer, n)
    
    return answer