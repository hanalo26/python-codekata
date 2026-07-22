# 모음사전
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/84512
# 알고리즘: 완전탐색
# 작성자: 백하은
# 작성일: 2026. 07. 22. 23:13:19

def solution(word):
    # 각 단어를 구성하는 알파벳 모음
    base = ['A', 'E', 'I', 'O', 'U']
    
    # 제작한 단어 저장
    dictionary = []
    
    # 단어를 제작하는 함수(dfs)
    def dfs(curr_word):
        # 1. 단어의 길이가 5를 초과하는가?
        if len(curr_word) > 5:
            # 다시 처음으로 돌아감
            return
        
        # 2. 현재 만들어진 단어가 빈 문자열이 아닌가?
        if curr_word != "":
            # 2-1. dictionary에 단어 추가
            dictionary.append(curr_word)
            
        # 3. A ~ UUUUU까지 뒤에 하나씩 붙여가면서 모든 단어 조합 생성
        for v in base:
            # curr_word에 v를 하나씩 붙인 단어를 dictionary에 추가
            dfs(curr_word+v) # 단어장에서는 단어들이 (2)에 의해 계속 추가됨
            
    # 첫 시작은 빈 문자열부터
    dfs("")
    
    
    # 주어진 단어가 사전에서 몇 번째에 있는가?
    answer = dictionary.index(word) + 1
    
    return answer