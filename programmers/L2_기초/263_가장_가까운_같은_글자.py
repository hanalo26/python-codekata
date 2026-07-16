# 가장 가까운 같은 글자
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/142086
# 알고리즘: 해시
# 작성자: 백하은
# 작성일: 2026. 07. 16. 12:17:03

def solution(s):
    answer = []
    
    # 각 글자별로 가장 최근에 등장한 인덱스를 저장할 딕셔너리
    seen = {}
    
    # 인덱스와 글자 동시 순회
    for idx, char in enumerate(s):
        if char not in seen:
            answer.append(-1)
        else:
            distance = idx - seen[char]
            answer.append(distance)
            
        # 글자 위치 업데이트
        seen[char] = idx
    
    return answer