# 택배상자
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131704
# 알고리즘: 스택
# 작성자: 백하은
# 작성일: 2026. 09. 29. 20:37:21

def solution(order):
    # 보조 컨베이어 벨트에 올라간 상자의 번호
    stack = []
    
    # 트럭에 실어야 하는 상자의 번호의 인덱스
    idx = 0
    
    # 메인 컨베이어 벨트에서 나오는 상자의 번호
    for n in range(1, len(order)+1):
        # 박스를 바로 보조 컨베이어 벨트에 올림 -> 올린 뒤에 바로 검사할 예정
        stack.append(n)
        
        # 트럭에 실어야 하는 상자 번호와 일치하는지 검사
        while stack and (stack[-1] == order[idx]):
            # 일치하는 경우
            stack.pop()
            idx += 1
    
    # 트럭에 실은 상자의 개수
    return idx