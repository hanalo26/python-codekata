# 숫자 짝꿍
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131128
# 알고리즘: 해시, 문자열
# 작성자: 백하은
# 작성일: 2026. 07. 29. 18:32:31

# 짝꿍이 되기 위한 조건1: X,Y에 공통으로 나타나는 숫자를 조합해서 만들 수 있는 가장 큰 수
# 짝꿍이 존재하지 않으면 -1
from collections import Counter

def solution(X, Y):
    cnt_X = Counter(X)
    cnt_Y = Counter(Y)
    
    answer = []
    
    # 0 ~ 9까지의 숫자 중에서 두 숫자에 존재하는 숫자를 찾으면 개수 -1씩해서 짝꿍을 만들기 위한 숫자 수집
    for i in range(9,-1,-1):
        char_i = str(i)
        
        # 두 숫자에 모두 존재한다면 둘 중 더 적은 개수만큼 양쪽에서 제거
        common_cnt = min(cnt_X[char_i], cnt_Y[char_i])
        if common_cnt > 0:
            answer.append(char_i * common_cnt)
            
    # 공통으로 나타나는 숫자가 없을 떄
    if not answer:
        return "-1"
    
    result = "".join(answer)
    
    if result[0] == "0":
        return "0"
    
    return result