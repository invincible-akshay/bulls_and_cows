# *********************** #
# @UTHOR: AKSHAY NEHE     #
# Date : 17-Apr-2019      #
# *********************** #
from itertools import product
from random import shuffle

"""
try:
    input
except:
    raw_input = input
try:
    from itertools import izip
except:
    izip = zip
"""

digits = '0123456789'
size = 6


def parse_score(score):
    score = score.strip().split(',')
    # print("score on splitting is: " + str(score))
    # print(tuple(int(s.strip()) for s in score))
    return tuple(int(s.strip()) for s in score)


def score_calc(guess, chosen):
    bulls = cows = 0
    new_guess = ()
    new_chosen = ()
    for i in range(size):
        if guess[i] == chosen[i]:
            bulls += 1
        else:
            new_guess += (guess[i],)
            new_chosen += (chosen[i],)

    for g, c in zip(new_guess, new_chosen):
        # print('g = ' + g + ' and c = ' + c)
        if g in new_chosen:
            cows += 1
    return bulls, cows


# choices = list(permutations(digits, size))
choices = [p for p in product(digits, repeat=size)]
shuffle(choices)
answers = []
scores = []

print("Playing Bulls & Cows with %i unique digits\n" % size)

while True:
    ans = choices[0]
    answers.append(ans)
    # print ("(Narrowed to %i possibilities)" % len(choices))
    score = input("Guess %2i is %*s. Answer (Bulls, cows)? "
                  % (len(answers), size, ''.join(ans)))
    score = parse_score(score)
    scores.append(score)
    # print("Bulls: %i, Cows: %i" % score)
    found = score == (size, 0)
    if found:
        print("Ye-haw!")
        break
    choices = [c for c in choices if score_calc(c, ans) == score]
    # print(choices)
    if not choices:
        print("Bad scoring? nothing fits those scores you gave:")
        print('  ' +
              '\n  '.join("%s -> %s" % (''.join(an), sc)
                          for an, sc in zip(answers, scores)))
        break
