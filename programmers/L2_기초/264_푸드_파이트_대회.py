# 푸드 파이트 대회
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/134240
# 알고리즘: 문자열
# 작성자: 백하은
# 작성일: 2026. 07. 16. 12:22:34

def solution(food):
    left = ""
    
    for i in range(1,len(food)):
        # 한 선수가 먹을 수 있는 양만큼 음식 번호(i)를 문자열로 만들어 배치
        cnt = food[i] // 2
        left += str(i)*cnt
    
    return left + "0" + left[::-1]