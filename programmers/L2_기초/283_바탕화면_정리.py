# 바탕화면 정리
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/161990
# 알고리즘: 시뮬레이션
# 작성자: 백하은
# 작성일: 2026. 07. 20. 17:30:53

def solution(wallpaper):
    # lux : 가장 위쪽 경계 (파일의 행번호 중 최솟값과 동일)
    # luy : 가장 왼쪽 경계 (파일의 열번호 중 최솟값과 동일)
    # rdx : 가장 아래쪽 경계 (파일의 행번호 중 최댓값+1과 동일)
    # rdy : 가장 오른쪽 경계 (파일의 열번호 중 최댓값+1과 동일)
        # 끝점은 파일 칸을 완전히 덮어야 하므로 +1이 되어야 함
    
    x_code = [] # x좌표
    y_code = [] # y좌표
    
    # 바탕화면 순회 (i,j)
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if "#" in wallpaper[i][j]:
                x_code.append(i)
                y_code.append(j)
                
    # lux, luy, rdx, rdy 찾기
    lux = min(x_code)
    luy = min(y_code)
    rdx = max(x_code) + 1
    rdy = max(y_code) + 1
    
    return [lux, luy, rdx, rdy]