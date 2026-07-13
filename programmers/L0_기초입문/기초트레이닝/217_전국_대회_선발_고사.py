# 전국 대회 선발 고사
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181851
# 알고리즘: 함수(메서드)
# 작성자: 백하은
# 작성일: 2026. 07. 13. 12:03:15

def solution(rank, attendance):
    candidate = []
    
    # 학생 번호(인덱스), 등수를 동시에 순회
    for idx, rn in enumerate(rank):
        if attendance[idx]:
            candidate.append((rn,idx))
    
    # 등수를 기준으로 오름차순 정렬
    candidate.sort()
    
    a = candidate[0][1] # 참석자 중 가장 높은 등수인 학생의 idx을 추출하는 코드
    b = candidate[1][1]
    c = candidate[2][1]
    
    return 10000*a + 100*b + c