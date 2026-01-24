# 숫자 야구
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/451808
# 작성자: 백하은
# 작성일: 2026. 01. 24. 14:18:53

def solution(n, submit):
    from random import sample

    # 후보 생성
    candidates = []
    for a in range(1, 10):
        for b in range(1, 10):
            if b == a: continue
            for c in range(1, 10):
                if c in (a, b): continue
                for d in range(1, 10):
                    if d in (a, b, c): continue
                    candidates.append(f"{a}{b}{c}{d}")

    # hint 계산
    def get_hint(secret, guess):
        strike = sum(1 for i in range(4) if secret[i] == guess[i])
        ball = sum(1 for i in range(4) if guess[i] in secret and secret[i] != guess[i])
        return strike, ball

    # submit 문자열 -> (strike, ball)
    def parse_hint(hint):
        s, b = hint.split()
        return int(s[:-1]), int(b[:-1])

    # 후보 필터링
    def filter_candidates(candidates, guess, strike, ball):
        return [c for c in candidates if get_hint(c, guess) == (strike, ball)]

    # 최적 guess 선택
    def select_best_guess(candidates):
        if not candidates:
            return None
        if len(candidates) <= 2:
            return candidates[0]

        sample_size = min(len(candidates), 300)
        guess_pool = sample(candidates, sample_size) if len(candidates) > sample_size else candidates

        best_guess = guess_pool[0]
        min_worst_case = float('inf')

        for guess in guess_pool:
            feedback_counts = {}
            for cand in candidates:
                fb = get_hint(cand, guess)
                feedback_counts[fb] = feedback_counts.get(fb, 0) + 1
            worst_case = max(feedback_counts.values())
            if worst_case < min_worst_case:
                min_worst_case = worst_case
                best_guess = guess

        return best_guess

    attempts = 0
    guess = select_best_guess(candidates)
    if guess is None:
        return -1

    while attempts < n and candidates:
        attempts += 1
        feedback_str = submit(int(guess))
        strike, ball = parse_hint(feedback_str)

        if strike == 4:
            return int(guess)

        candidates = filter_candidates(candidates, guess, strike, ball)
        if not candidates:
            return -1

        guess = select_best_guess(candidates)
        if guess is None:
            return -1

    return int(candidates[0]) if candidates else -1