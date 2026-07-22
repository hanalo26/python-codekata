# 모음사전
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/84512
# 알고리즘: 완전탐색
# 작성자: 백하은
# 작성일: 2026. 07. 23. 00:58:41

def solution(word):
    # 알파벳 모음
    base = ['A', 'E', 'I', 'O', 'U']
    
    # 단어 사전
    words = []
    
    # 모음을 하나씩 이어붙이면서 단어 사전을 만드는 함수
    def make_words(current_word):
        # 입력된 단어의 길이가 5 미만인가?
        # - 5보다 길면 처음으로 돌아가야 함
        if len(current_word) > 5:
            return
        
        # 입력된 단어가 빈 문자열인가?
        # - 빈 문자열이 아니라면 단어 사전에 추가함
        if current_word != "":
            words.append(current_word)
        
        # 모든 단어 조합 생성
        for w in base:
            # 두 조건문을 활용해 단어 사전에 계속 추가
            make_words(current_word+w)
        
    # 내부 함수 사용, 시작은 빈 문자열
    make_words("")
    
    # 사전 내에서 몇 번째 단어인지 찾기
    answer = words.index(word)
    
    # 답
    return answer