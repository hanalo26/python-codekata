# 달리기 경주
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/178871
# 알고리즘: 해시
# 작성자: 백하은
# 작성일: 2026. 07. 31. 14:33:23

def solution(players, callings):
    # 선수 이름-현재 등수, 등수-선수 이름 형태의 딕셔너리 생성
    # 등수 변경 전, 등수 변경 후로 구분
    name_to_rank = {}
    rank_to_name = {}
    
    for rank, name in enumerate(players):
        name_to_rank[name] = rank
        rank_to_name[rank] = name
        
    # 경기 진행 중(추월 발생)
    for name in callings:
        cur_rank = name_to_rank[name] # 추월한 선수
        # 추월당한 선수의 등수와 이름
        prev_rank = cur_rank - 1
        prev_name = rank_to_name[prev_rank]
        
        # 추월당한 등수 반영
        name_to_rank[name] = prev_rank
        name_to_rank[prev_name] = cur_rank
        
        rank_to_name[prev_rank] = name
        rank_to_name[cur_rank] = prev_name
        
    # 최종 등수    
    answer = []
    
    for i in range(len(players)):
        answer.append(rank_to_name[i])
    
    return answer