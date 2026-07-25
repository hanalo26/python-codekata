# 최솟값 만들기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12941
# 작성자: 백하은
# 작성일: 2026. 07. 25. 19:01:18

def solution(A,B):
    answer = 0

    a = sorted(A) # 오름차순으로 정렬
    b = sorted(B, reverse=True) # 내림차순으로 정렬
    
    # (A배열에서 제일 작은 수 * B배열에서 가장 큰 수)의 총핣이 가장 작아짐
    for i in range(len(a)):
        answer += a[i] * b[i]

    return answer