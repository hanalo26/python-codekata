# 등수 매기기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120882
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 05. 20. 10:39:55

def solution(score):
    # 각 학생들의 평균 점수가 담긴 리스트
    total_score = [sum(s)/2 for s in score]
    
    # 평균점수를 내림차순으로 정렬
    answer = sorted(total_score, reverse=True)
    return [answer.index(i)+1 for i in total_score]