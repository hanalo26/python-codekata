# 햄버거 만들기
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/133502
# 알고리즘: 스택
# 작성자: 백하은
# 작성일: 2026. 07. 30. 13:59:16

"""
야채(2)
빵(1)
고기(3)

햄버거 제조 순서: 1-2-3-1
"""


def solution(ingredient):
    answer = 0
    stack = [] # 재료
    
    for item in ingredient:
        stack.append(item)
        # 제일 뒤에 있는 원소 4개가 정해진 순서대로 등장하는지 검사
        if len(stack) >= 4 and stack[-4:] == [1,2,3,1]:
            answer += 1
            for _ in range(4):
                stack.pop()
    
    return answer