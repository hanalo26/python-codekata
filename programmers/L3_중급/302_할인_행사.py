# 할인 행사
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131127
# 알고리즘: 해시, 슬라이딩윈도우
# 작성자: 백하은
# 작성일: 2026. 08. 08. 13:39:18

"""
정현이가 원하는 제품: want
정현이가 원하는 제품의 수량: number
XYZ 마트에서 할인하는 제품: discount
"""
from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    # 1. 내가 원하는 제품과 수량을 딕셔너리로 만듦
    target = {}
    
    for w,n in zip(want, number):
        target[w] = n
    
    # 2. 10일 연속으로 구매해야 하므로, 시작 가능한 날짜 범위를 순회
    # 회원 자격이 10일간 유지되므로, discount 배열을 10개씩 잘라서 확인
    m = len(discount)
    
    for i in range(m-10+1):
        # 2-1. 10일 동안 할인하는 제품들의 개수를 센다
        cur_10_days = Counter(discount[i:i+10])
        
        # 2-2. 10일간의 할인 품목 구성이 내가 원하는 구성과 일치하는지 확인
        if cur_10_days == target:
            answer += 1
        
    return answer