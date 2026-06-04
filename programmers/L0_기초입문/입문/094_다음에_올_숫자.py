# 다음에 올 숫자
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120924
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 06. 04. 21:48:43

def solution(common):
    # 등차수열일때
    if (common[1]-common[0]) == (common[2]-common[1]):
        return common[-1] + (common[1]-common[0])
    # 등비수열일때
    else:
        return common[-1] * (common[1]//common[0])