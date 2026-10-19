# 연속된 부분 수열의 합
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/178870
# 알고리즘: 투포인터
# 작성자: 백하은
# 작성일: 2026. 10. 19. 18:43:23

"""
1. (left, right)를 모두 사용한 이유
- 수열 전체를 일일이 자르면서 합을 구하면 시간이 초과될 수 있으므로 범위를 정해서 계산하도록 하기 위해서

2. k에 따라 최종 답을 출력하는 과정
- k보다 작다면 right를 오른쪽으로 한 칸 옮김
- k보다 크다면 left를 오른쪽으로 한 칸 옮김
- k와 동일하다면 일단 정답으로 등록해두고 혹시 더 짧은 길이의 수열이 있는지 확인하기 위해 left를 오른쪽으로 한 칸 옮겨 확인
"""

def solution(sequence, k):
    # 포인터 지정
    left = 0
    right = 0
    
    # left, right로 확인 중인 부분 수열의 합
    # - 초기에는 left=right=0이므로 0번째 값으로 저장
    cur_sum = sequence[0]
    
    # 정답을 저장할 변수
    # - 초기에는 전체 sequence의 길이로 지정
    best_left = 0
    best_right = len(sequence)-1
    
    # right를 수열의 끝까지 이동시키면서 확인
    while right < len(sequence):
        # 만약 현재 부분 수열의 합이 목표값(k)과 같다면? -> 현재 수열의 길이 계산
        if cur_sum == k:
            cur_length = right-left
            
            # 앞서 저장된 수열의 길이보다 짧으면 변경하고, 길이가 같다면 시작 인덱스가 작은 것을 채택 (단, left는 항상 오른쪽으로 이동하므로 먼저 찾은 것을 채택해야 해 같은 경우는 값을 변경할 필요 없음)
            if cur_length < (best_right-best_left):
                best_left = left
                best_right = right
            
            # 다음 탐색 시작
            cur_sum = cur_sum - sequence[left]
            left += 1
            
        # k보다 작다면?    
        elif cur_sum < k:
            right += 1
            # right가 수열의 길이를 벗어났는지 검사
            if right < len(sequence):
                cur_sum += sequence[right]
        
        # k보다 크다면?
        elif cur_sum > k:
            cur_sum = cur_sum - sequence[left]
            left += 1
    
    return [best_left, best_right]