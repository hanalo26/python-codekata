# 혼자 놀기의 달인
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131130
# 알고리즘: 그래프, 시뮬레이션
# 작성자: 백하은
# 작성일: 2026. 11. 10. 16:44:04

"""
[게임의 규칙]
1. 1번부터 N번까지의 상자가 있고, 각 상자 안에는 무작위로 섞인 카드(숫자)가 들어 있음
2. 임의의 상자를 열어 카드 번호를 확인하고, 그 카드 번호에 해당하는 상자를 계속 열음
3. 이미 열려 있는 상자를 만날 때까지 열고 그룹을 묶는데, 이 과정이 하나의 cycle이 됨
4. 첫 번째 그룹을 만들고 남은 상자가 있다면, 그중 하나를 골라 같은 방식으로 두 번째 그룹을 만듦
5. 최종 점수 = (1번 상자 그룹의 개수) × (2번 상자 그룹의 개수)의 최댓값
6. 만약 상자가 한 그룹으로 전부 다 열려버려서 두 번째 그룹을 만들 수 없다면 점수는 0점

[메모]
1. 배열의 인덱스는 0부터 시작, 카드는 1부터 시작
2. cards[i] = i + 1번 상자에 담긴 카드에 적힌 숫자

3. 게임 진행 방식
    - 첫번째 상자를 열었는데, 8번 카드가 나오면 8번째 상자를 열고 거기서 4번 카드가 나오면 4번째 상자를 여는 걸 반복하는 방식
"""

def solution(cards):
    n = len(cards)
    visited = [False]*n
    group_size = [] # 상자 그룹의 크기(한 그룹당 상자의 개수)
    
    for i in range(n):
        # 아직 열지 않은 상자라면 새로운 그룹(사이클) 탐색 시작
        if not visited[i]:
            cur_group_size = 0
            curr = i
            
            # 이미 방문한 상자를 만날 때까지 계속 열기
            while not visited[curr]:
                visited[curr] = True
                cur_group_size += 1
                # 다음에 열어야 할 상자의 번호
                curr = cards[curr] - 1
            
            group_size.append(cur_group_size)
            
    # 내림차순으로 정렬해 최종 점수가 가장 큰 값이 되도록 만듦
    group_size.sort(reverse=True)
    
    # 그룹이 2개 이상이면 상위 두 개의 곱 반환, 아니면 0 반환
    if len(group_size) >= 2:
        return group_size[0] * group_size[1]
    else:
        return 0