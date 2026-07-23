# H-Index
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42747
# 알고리즘: 정렬
# 작성자: 백하은
# 작성일: 2026. 07. 24. 00:47:20

# h: 어느 과학자의 H-Index를 나타내는 값
# h번 이상 인용된 논문이 h편 이상 있고, 그렇지 않은 것도 h편 이하로 있다 -> 이떄의 h가 H-Index가 됨

# 발표한 논문별 인용수를 기준으로 정렬 -> h에 1부터 넣어가면서 비교.
# 정렬한 뒤에 h번째에 있는 논문의 인용수가 h이상인지 확인 -> 이게 되는 이유: h번째에 있는 논문의 인용수가 h보다 크면 내림차순 정렬을 했기 때문에 앞에 있는 논문들의 인용수는 당연히 h보다 큼
# 위 조건이 깨지면 stop하고 h를 return

def solution(citations):
    citations.sort(reverse=True)
    
    for idx in range(len(citations)):
        h = idx + 1
        
        if citations[idx] < h:
            return h - 1
            
    # 반복문이 종료되었음에도 불구하고 조건이 깨지지 않는다면?
    return len(citations)