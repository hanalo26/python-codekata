# 로또의 최고 순위와 최저 순위
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/77484
# 알고리즘: 해시
# 작성자: 백하은
# 작성일: 2026. 07. 20. 16:31:14

def solution(lottos, win_nums):
    correct_cnt = 0
    zero_cnt = lottos.count(0)
    
    for i in lottos:
        if i in win_nums:
            correct_cnt += 1
            
    max_correct = correct_cnt + zero_cnt
    min_correct = correct_cnt
    
    # 등수를 반환하는 함수
    def get_ranks(corrects):
        rn = 7 - corrects
        
        if rn < 6:
            return rn
        else:
            return 6
    return [get_ranks(max_correct), get_ranks(min_correct)]