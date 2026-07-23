# 큰 수 만들기
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42883
# 알고리즘: 그리디, 스택
# 작성자: 백하은
# 작성일: 2026. 07. 23. 15:34:40

def solution(number, k):
    
    # 남겨둔 숫자를 저장하는 곳
    answer = []
    
    # 주어진 문자열을 앞에서부터 answer에 저장하되 새롭게 읽은 원소가 앞서 읽은 것보다 크다면 k가 허락하는만큼 버린다
    for num in number:
        # answer가 비어있지 않고, k가 양수이며, 맨 뒤에 있는 글자가 num보다 작다면 삭제
        while answer and k > 0 and answer[-1] < num:
            answer.pop() # 맨 뒤에 있는 요소 삭제
            k = k - 1
            
        answer.append(num)
        
    # k가 아직도 남아있다면?
    if k > 0:
        # 뒤에서부터 k개 버림
        answer = answer[:-k]
        
    return "".join(answer)