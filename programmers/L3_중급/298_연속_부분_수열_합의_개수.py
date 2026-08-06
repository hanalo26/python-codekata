# 연속 부분 수열 합의 개수
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131701
# 알고리즘: 해시, 슬라이딩윈도우
# 작성자: 백하은
# 작성일: 2026. 08. 06. 15:16:45

def solution(elements):
    # 훤형 수열의 원소 개수
    n = len(elements)
    
    # 첫 번째 원소와 마지막 원소가 연결되어 있음을 나타내기 위해 2를 곱함
    extended_elements = elements * 2
    
    sums = set() # 서로 다른 수를 더했을 때, 같은 수가 나오면 제거
    
    # 부분 수열의 합
    # 부분 집합의 길이에 따라 하나씩 늘려가며 계산
    for length in range(1,n+1):
        for start_point in range(n):
            sub_sum = sum(extended_elements[start_point:start_point+length])
            sums.add(sub_sum)
            
    return len(sums)