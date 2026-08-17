# 롤케이크 자르기
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/132265
# 알고리즘: 해시
# 작성자: 백하은
# 작성일: 2026. 08. 17. 16:45:48

from collections import Counter

def solution(topping):
    answer = 0
    
    # 철수가 먹는 롤케이크에 올라가는 토핑 가짓수
    Chu = set()
    
    # 동생이 먹는 롤케이크에 올라가는 토핑 가짓수
    ## {토핑 종류:개수}의 형식으로 저장
    Bro = Counter(topping)
    
    # 칼로 자르는 위치(=인덱스)를 바꿔가면서 테스트
    for i in topping:
        Chu.add(i) # 토핑이 하나 생김
        Bro[i] = Bro[i] - 1 # 토핑이 하나 사라짐
        
        if Bro[i] == 0: # 모든 토핑 분배 완료
            del Bro[i]
            
        if len(Chu) == len(Bro):
            answer += 1
    
    return answer