# n^2 배열 자르기
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/87390
# 알고리즘: 수학, 시뮬레이션
# 작성자: 백하은
# 작성일: 2026. 08. 07. 18:28:03

# i는 1차원 배열의 인덱스
# 행(Row) 번호[r]: i // n
# 열(Column) 번호[c]: i % n

# 2차원 좌표에서 각 위치에 대입하는 값
# (r,c) -> max(r,c)+1

def solution(n, left, right):
    answer = []
    
    for i in range(left, right+1):
        r = i // n
        c = i % n
        value = max(r,c) + 1
        answer.append(value)
    
    return answer