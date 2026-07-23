# 의상
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42578
# 알고리즘: 해시, 수학
# 작성자: 백하은
# 작성일: 2026. 07. 23. 21:38:56

# 의상의 종류별로 여러가지 의상이 존재할 수 있다
# 특정 의상의 종류를 아예 안 입는다는 선택지도 있다, 단 모든 의상을 안 입는 날은 없다
from collections import Counter

def solution(clothes):
    
    # 1. 각 의상의 종류별로 몇 개의 의상이 있는가?
    c = []
    for name, kind in clothes:
        c.append(kind)
        
    cloth = Counter(c)
        
    # 2. 의상을 입는 조합의 개수 (단, 모든 의상을 입지 않는 경우는 제외해야 함)
    answer = 1
    
    # 여기서는 안 입는다는 선택지도 넣어야 함
    for n in cloth.values():
        answer = answer * (n+1)
        
    # 답, 아무것도 입지 않은 경우는 뺴야 함
    return answer -1