# 치킨 쿠폰
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120884
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 05. 20. 10:27:20

def solution(chicken):
    if chicken > 0:
        # 10장으로 서비스를 받지만, 서비스 치킨도 쿠폰을 주므로 쿠폰 9장을 쓰는 것과 동일
        # 서비스 치킨을 받았을 때, 최소 1장의 쿠폰은 남아 있으므로 (전체 치킨 수-1)
        return (chicken - 1) // 9
    else:
        return 0