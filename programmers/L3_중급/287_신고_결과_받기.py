# 신고 결과 받기
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/92334
# 알고리즘: 해시, 시뮬레이션
# 작성자: 백하은
# 작성일: 2026. 08. 01. 15:05:09

# 같은 사람이 A를 여러 번 고발하더라도, 1번 고발한 것으로 처리
# 한 번에 여러 명 신고 가능
# A가 k번 이상 신고당하면 이용 정지 -> A를 신고했던 모든 유저들에게 해당 사실 통보

def solution(id_list, report, k):
    # 중복 신고 제거
    report = set(report)
    
    # 딕셔너리 생성: {신고당한 유저:신고당한 횟수}, {신고한 유저:자신이 신고한 유저의 집합}
    reported_cnt = {}
    reports_user = {}
    
    for id in id_list:
        reported_cnt[id] = 0
        reports_user[id] = set()
    
    # 유저별 신고 정보 집계
    for r in report:
        reporter, reported = r.split()
        reported_cnt[reported] += 1
        reports_user[reporter].add(reported) 
        
    # k번 이상 신고당해서 정지당한 유저들의 집합
    banned_users = set()
    
    for u, c in reported_cnt.items():
        if c >= k:
            banned_users.add(u)
    
    # 각 유저별로 정지당한 유저를 신고한 횟수 계산(=받을 메일 수)
    answer = []
    for u in id_list:
        # 내가 신고한 유저와 정지당한 유저의 교집합의 길이
        mailed = len(reports_user[u] & banned_users)
        answer.append(mailed)
    
    return answer