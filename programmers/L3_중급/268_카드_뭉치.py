# 카드 뭉치
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/159994
# 알고리즘: 스택/큐
# 작성자: 백하은
# 작성일: 2026. 07. 22. 15:12:22

def solution(cards1, cards2, goal):
    # cards1의 인덱스
    idx1 = 0
    
    # cards2의 인덱스
    idx2 = 0
    
    # goal의 단어를 하나씩 가져와서 검사
    for word in goal:    
        # cards1에서 가져올 수 있는 경우, 단 idx1이 cards1의 길이보다 커지지 않도록 주의
        if idx1 < len(cards1) and cards1[idx1] == word:
            idx1 += 1
        
        # cards2에서 가져올 수 있는 경우, 단 idx2이 cards2의 길이보다 커지지 않도록 주의
        elif idx2 < len(cards2) and cards2[idx2] == word:
            idx2 += 1
        
        # 두 카드에서 모두 가져올 수 없는 경우 (순서를 바꾸는 것은 안됨)
        else:
            return "No"
        
    # 두 카드에서 순서대로 가져와서 만들 수 있는 경우
    return "Yes"