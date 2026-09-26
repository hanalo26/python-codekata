# 쿼드압축 후 개수 세기
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/68936
# 알고리즘: 분할정복
# 작성자: 백하은
# 작성일: 2026. 09. 26. 16:10:43

def solution(arr):
    answer = [0, 0] # [0의 개수, 1의 개수]
    
    # 탐색할 영역의 좌상단 위치의 좌표 = (x,y)
    # 탐색할 영역의 한변의 길이
    def compress(x,y,length):
        first_val = arr[x][y]
        
        # 탐색하고 있는 영역의 모든 값이 first_val과 같다면 하나로 압축
        # 지정된 (x, y) 위치부터 length 범위 안의 모든 원소가 첫 번째 값 first_val과 같은지 검사
        for i in range(x, x+length):
            for j in range(y, y+length):
                # first_val과 다른 값이 있다면 half = length // 2 크기의 4개 영역으로 쪼개어 각각 다시 검사
                if arr[i][j] != first_val:
                    half = length // 2
                    compress(x, y, half)  # 1사분면 위치
                    compress(x, y + half, half) # 2사분면 위치
                    compress(x + half, y, half) # 3사분면 위치
                    compress(x + half, y + half, half) # 4사분면 위치
                    return
                
        # 영역 전체가 동일한 값이면 압축 성공 -> 해당 값의 카운트 +1
        answer[first_val] += 1
        
    # (0,0)부터 차례대로 검사
    # length = len(arr)
    
    compress(0,0,len(arr))
    
    return answer