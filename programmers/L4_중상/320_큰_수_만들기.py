# 큰 수 만들기
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42883
# 알고리즘: 그리디, 스택
# 작성자: 백하은
# 작성일: 2026. 07. 23. 19:03:06

def solution(number, k):
    # 1. number를 앞에서부터 하나씩 떼어오면서 정답에 저장.
    #  - k는 제거해야 하는 숫자이므로 숫자를 정답에서 뺄 때마다 -1
    #  - 뒤에 오는 숫자는 앞에서 검사한 숫자보다 크거나 같아야 함
    #  - number에 있는 숫자를 다 읽어서 정답을 만들었음에도 k가 남아있다면 정답에서 k개만큼 뒤에서 뺀다
    
    answer = []
    
    for num in number:
                
        # answer이 비어있지 않음+새롭게 읽은 숫자는 직전에 읽은 숫자보다 큼 + k가 아직 남아있음
        while answer and num > answer[-1] and k > 0:
            answer.pop()
            k = k - 1
        
        # answer이 비어있거나 나머지 조건 중 하나라도 충족하지 않는다면
        answer.append(num)
        
    # 반복문을 다 돌았음에도 k > 0 이라면?
    if k > 0:
        answer = answer[:-k]
        
        
    # 정답
    return "".join(answer)