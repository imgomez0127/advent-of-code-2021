paren_pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}
paren_scores = {
    '': 0,
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
autocomplete_scores = {
    '': 0,
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}
with open('input.txt', 'r') as f:
    arr = [line.strip() for line in f]

def balanced(s):
    q = []
    if s[0] in paren_pairs:
        q.append(paren_pairs[s[0]])
    else:
        return False, s[0]
    i = 1
    while i < len(s):
        if s[i] not in paren_pairs:
            if s[i] != q.pop():
                return False, s[i]
        else:
            q.append(paren_pairs[s[i]])
        i += 1 
    return True, q

def score_q(q):
    score = 0
    print(list(reversed(q)))
    for paren in reversed(q):
        score *= 5
        score += autocomplete_scores[paren]
    return score

score = [paren_scores[paren] for is_balanced, paren in map(balanced, arr) 
         if not is_balanced]
print(score)
print(sum(score))
score2 = [score_q(q) for is_balanced, q in map(balanced, arr) if is_balanced]
print(score2)
print(sorted(score2)[len(score2)//2])
