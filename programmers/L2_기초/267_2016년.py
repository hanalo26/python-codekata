# 2016년
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12901
# 알고리즘: 수학
# 작성자: 백하은
# 작성일: 2026. 07. 18. 14:21:23

def solution(a, b):
    # 2016년 1~12월까지 각 달의 일수
    months = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    # 1/1은 금요일이므로 금요일이 인덱스 0번
    days = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    
    # a월 b일은 1/1 제외하고 며칠 뒤인지 계산할 예정
    total_days = sum(months[:a-1])+(b-1)
    
    # 7일로 나눈 뒤, 나머지만큼 이동한 인덱스로 요일을 구함
    return days[total_days%7]