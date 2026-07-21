# 최댓값과 최솟값
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12939
# 알고리즘: 문자열
# 작성자: 백하은
# 작성일: 2026. 07. 21. 13:16:22

def solution(s):
    nums = list(map(int,s.split()))
    
    return f"{min(nums)} {max(nums)}"