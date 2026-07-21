# 삼총사
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131705
# 알고리즘: 완전탐색
# 작성자: 백하은
# 작성일: 2026. 07. 21. 13:49:35

def solution(number):
    answer = 0
    
    # 반복문으로 중복없이 3개를 뽑기 위한 구문 작성
    # i < j < k의 순서를 유지하도록 하여 동일한 조합이 중복해서 카운트되지 않도록 함
    n = len(number)
    
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    
    return answer