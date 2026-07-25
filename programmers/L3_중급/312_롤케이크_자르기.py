# 롤케이크 자르기
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/132265
# 알고리즘: 해시
# 작성자: 백하은
# 작성일: 2026. 07. 25. 19:36:19

# 케이크의 크기 -> 즉, 슬라이싱된 리스트의 길이는 상관 없음
# 슬라이싱된 리스트에 동일한 가짓수의 토핑이 올라가기만 하면 됨 -> 구체적인 종류까지 같을 필요는 없음
# 공평하게 나눌 수 없다면 0을 반환
from collections import Counter

def solution(topping):
    answer = 0
    
    # 철수
    Chul = set()
    
    # 동생
    Bro = Counter(topping)
    
    # 1. 칼로 자르는 위치를 옮겨가면서 확인
    for i in topping:
        Chul.add(i)
        Bro[i] = Bro[i] - 1
        
        if Bro[i] == 0:
            del Bro[i]
        
        if len(Chul) == len(Bro):
            answer += 1

    return answer