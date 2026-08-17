# 모음사전
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/84512
# 알고리즘: 완전탐색
# 작성자: 백하은
# 작성일: 2026. 08. 17. 16:40:30

def solution(word):
    # 알파벳 모음
    base = ['A', 'E', 'I', 'O', 'U']
    
    # 단어사전 제작
    dict_alpha = []
    
    # 단어사전을 만드는 함수
    def make_word(cur_word):
        # 빈 문자열이 입력되었는가?
        ## 빈문자열이 아니라면 사전에 추가
        if cur_word != "":
            dict_alpha.append(cur_word)
        
        # 입력된 단어의 길이가 5 이하인가?
        ## 5글자가 입력되면 사전에 기록한 뒤, 마지막 글자 삭제
        if len(cur_word) == 5:
            return
        
        # 두 조건문을 활용해 모든 모음을 사용해 단어를 만드는 반복문 삽입(내부 함수에 포함된 부분)
        for w in base:
            make_word(cur_word+w)
    
    # 내부 함수 사용
    make_word("")
    
    answer = dict_alpha.index(word) + 1
    
    return answer