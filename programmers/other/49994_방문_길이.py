# 방문 길이
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/49994
# 작성자: 백하은
# 작성일: 2026. 07. 25. 20:04:12

# 갔다가 되돌아 오는 건 +1로 카운트 (a->b, b->a인 경우)
# 이미 다녀온 점에서 다녀온 점으로 이동하는 것은 이동은 하되, 카운트하지 X

def solution(dirs):
    # 캐릭터의 이동거리
    answer = 0
    
    # dirs에 따른 이동 방향키
    directions = {
        "U": (0,1),
        "D": (0,-1),
        "R": (1,0),
        "L": (-1,0)
    }
    
    # 지나온 길
    visit = set()
    
    # 시작점
    x, y = (0,0)
    
    # 캐릭터 이동 시작
    for d in dirs:
        dx, dy = directions[d]
        nx = x + dx
        ny = y + dy
        
        # 격자를 벗어나는지 확인
        if not (-5 <= nx <= 5 and -5 <= ny <= 5):
            # 벗어난다면 무시
            continue
        
        # 처음 지나가는 길인지 확인
        if ((x,y),(nx,ny)) not in visit:
            # 처음 지나가는 길이라면 이동횟수+1
            answer += 1
            
            # visit에 추가
            visit.add(((x,y),(nx,ny)))
            visit.add(((nx,ny),(x,y)))
            
        # 캐릭터의 현재 위치 갱신
        x = nx
        y = ny
    
    return answer