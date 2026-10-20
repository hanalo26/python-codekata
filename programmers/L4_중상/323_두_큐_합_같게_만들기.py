# 두 큐 합 같게 만들기
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/118667
# 알고리즘: 큐, 투포인터
# 작성자: 백하은
# 작성일: 2026. 10. 20. 16:35:24

from collections import deque

def solution(queue1, queue2):
    #1.두 큐의 모든 원소의 합이 홀수라면 정확하게 절반을 나누는 것은 불가능 -> -1을 반환해야 함
    total_sum = sum(queue1) + sum(queue2)
    
    if total_sum % 2 != 0:
        return -1
    
    # 두 큐의 합이 짝수 -> 각 큐를 구성하는 원소의 합 = total_sum//2
    
    target = total_sum//2
    
    #2. 효율적인 pop/insert를 위해 deque로 전환
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    #3. q1을 구성하는 원소의 합, pop/insert 작업 횟수
    sum_q1 = sum(queue1)
    cnt = 0
    
    #4. 허용되는 최대 작업 횟수
    # - 만약에 이 문제가 풀리는 것이라면 숫자가 아무리 복잡해도 전체 길이의*3 만큼 반복하면 반드시 답이 나온다는 원리가 있다고 함
    # 내가 놓친 부분: 검사 횟수를 어떻게 제한할 것인가?
    max_limit = len(queue1)*3
    
    #5. 두 큐의 합이 목표값과 같아질 때까지 반복
    while cnt <= max_limit:
        
        if sum_q1==target:
            return cnt
        
        elif sum_q1>target:
            value = q1.popleft()
            q2.append(value)
            sum_q1 = sum_q1-value
            
        elif sum_q1<target:
            value = q2.popleft()
            q1.append(value)
            sum_q1 = sum_q1+value
            
        cnt+=1
        
    return -1
            