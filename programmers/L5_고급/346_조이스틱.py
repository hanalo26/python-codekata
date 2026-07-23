# 조이스틱
# 프로그래머스 L5 (고급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42860
# 알고리즘: 그리디
# 작성자: 백하은
# 작성일: 2026. 07. 23. 16:17:37

def solution(name):
    n = len(name)
    
    # 1. 알파벳 변경(상하 조작)
    up_down = 0
    
    for c in name:
        up = ord(c) - ord("A") # a,b,c 순서로 움직일때
        down = 26 - up # a,z,y 순서로 움직일때
        up_down += min(up, down)
    
    
    # 2. 커서 위치 변경 (좌우 조작)
    # 0번째와 n-1번째를 연결한다면? -> A가 연속되어있을 때 해당 구간을 피해 갔다가 돌아옴
    
    # 초기값은 뒤로가지 않았을 때 0 -> n-1번째로 이동하는 횟수로 작성
    move = n-1
    
    # 어느 A 구간에서 잘라야 최선인지는 미리 알 수 없으므로 전부 시도
    for i in range(n):
        # i 바로 뒤에 이어지는 A들을 건너뛴다
        # j는 그 A 덩어리 너머에서 처음 만나는 'A가 아닌 글자'의 위치다
        j = i+1
        while j < n and name[j] == "A":
            j+=1
        
        # 왼쪽으로 갔을 떄, 오른쪽으로 갔을 때 이동횟수 비교
        right = i
        left = n - j
        
        move = min(move, right*2+left, left*2+right)
        
    # 답
    return up_down + move