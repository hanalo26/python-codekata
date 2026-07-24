# 큰 수 만들기
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42883
# 알고리즘: 그리디, 스택
# 작성자: 백하은
# 작성일: 2026. 07. 24. 20:01:04

def solution(number, k):
    # numbers의 인덱스 순서를 지켜야 함 -> 앞에 오는 숫자는 뒤에 있는 숫자보다 인덱스가 작아야 함 -> 반복문으로 하나씩 비교하면서 빈 리스트에 쌓아야겠다.
    # 직전에 쌓은 숫자보다 검사중인 숫자가 큰 경우에 삽입하고, 직전에 쌓은 숫자를 버림 + K는 1 감소
    # 숫자는 k개만 버리면 됨 
    answer = []
    
    for i in number:
        
        # answer가 비어있지 않고, 직전에 쌓은 숫자보다 크며, K != 0일때
        while answer and k > 0 and answer[-1] < i:
            answer.pop()
            k = k - 1
            
        answer.append(i)
    
    
    # k != 0이면
    if k > 0:
        answer = answer[:-k]
    
    return "".join(answer)