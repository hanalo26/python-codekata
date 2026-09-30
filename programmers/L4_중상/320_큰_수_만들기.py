# 큰 수 만들기
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42883
# 알고리즘: 그리디, 스택
# 작성자: 백하은
# 작성일: 2026. 09. 30. 16:10:20

def solution(number, k):
    # 하나씩 담아 새로운 값과 크기를 비교하면서 최종 출력 숫자만 남길 예정 
    answer = []
    
    for n in number:
        # answer에 숫자가 있고, k는 0이 아니며, 저장된 숫자 중 맨 뒤 숫자가 현재보다 작으면 맨 뒤 숫자 제거
        while answer and k != 0 and answer[-1] < n:
            answer.pop()
            k = k-1
            
        # 현재 숫자를 answer에 추가
        answer.append(n)
        
    # k를 완전히 소진하지 못한 경우 -> 뒤에서부터 k개 제거
    if k > 0:
        answer = answer[:-k]
    
    # 리스트 내부 숫자를 하나의 문자열로 통합
    return "".join(answer)