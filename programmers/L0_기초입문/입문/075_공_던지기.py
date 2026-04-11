# 공 던지기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120843
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 04. 11. 19:32:33

def solution(numbers, k):
    # 첫 번째 사람은 지정되어 있으니 k번째
    # 던지는 사람에게 가기 위해서는 k-1번 이동해야 함 
    # 따라서, 이동거리는 2*(k-1)이고 이걸 전체 인원수로 나눈 나머지가 인덱스가 됨 
    # 이유: 마지막 인덱스와 0번 인덱스는 원형으로 앉아 바로 옆에 있기 때문에 최종 인덱스틑 n바퀴를 돌더라도 결국 나머지만큼 이동한 것과 같기 때문에 
    answer = (k-1) * 2 % len(numbers)
    return numbers[answer]