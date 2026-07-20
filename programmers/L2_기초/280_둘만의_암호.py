# 둘만의 암호
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/155652
# 알고리즘: 문자열
# 작성자: 백하은
# 작성일: 2026. 07. 20. 16:56:28

def solution(s, skip, index):
    answer = []
    
    # skip에 포함된 알파벳을 지운 알파벳 리스트 제작
    all_alpha = "abcdefghijklmnopqrstuvwxyz"
    filtered_alpha = []
    
    for char in all_alpha:
        if char not in skip:
            filtered_alpha.append(char)
            
    len_of_filtered_alpha = len(filtered_alpha)
    
    # 변환할 문자열 s 순회
    for txt in s:
        # txt가 몇 번째 인덱스에 존재하는지 확인
        correct_idx = filtered_alpha.index(txt)
        
        # index만큼 이동한 뒤,  필터된 알파벳 리스트의 길이를 넘어가면 처음으로 순환하도록 나머지 연산(%) 적용
        new_idx = (correct_idx + index) % len_of_filtered_alpha
        
        answer.append(filtered_alpha[new_idx])
        
    return "".join(answer)