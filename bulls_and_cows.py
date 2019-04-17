# *********************** #
# @UTHOR: AKSHAY NEHE     #
# Date : 17-Apr-2019      #
# *********************** #
from itertools import product
from random import shuffle
from random import choice


# Valid digits
digits = '0123456789'
# Size of secret
size = 4


def parse_score(input_score):
    """Parses the score provided by player to return a tuple of (bulls, cows)

        Parameters:
        score (str): Score given input by the user

        Returns:
        tuple(int):Returning tuple of (bulls, cows)

    """
    input_score = input_score.strip().split(',')
    return tuple(int(s.strip()) for s in input_score)


def score_giver(secret, guessed_code):
    """Scores a guess against the secret and returns a tuple of (bulls, cows)

            Parameters:
            secret (str): Chosen secret for scoring
            guessed_code (str): The guess to be scored against the secret

            Returns:
            tuple(int):Returning tuple of (bulls, cows)

    """
    bulls = cows = 0
    secret_occ = [0] * 10
    guess_occ = [0] * 10
    new_secret = ()
    new_guess = ()
    for i in range(len(secret)):
        if secret[i] == guessed_code[i]:
            bulls += 1
        else:
            new_secret += (secret[i],)
            secret_occ[int(secret[i])] += 1
            new_guess += (guessed_code[i],)
            guess_occ[int(guessed_code[i])] += 1
    for i in range(10):
        if secret_occ[i] != 0 and secret_occ[i] <= guess_occ[i]:
            cows += secret_occ[i]
        elif guess_occ[i] != 0 and guess_occ[i] <= secret_occ[i]:
            cows += guess_occ[i]
    return bulls, cows


def code_maker(code_size):
    secret_code = ''.join(choice(digits) for i in range(code_size))
    return secret_code


print("Playing for secret of size = %d" % size)
chosen_secret = code_maker(size)
print("Chosen secret : %s" % chosen_secret)
choices = [p for p in product(digits, repeat=size)]
shuffle(choices)
answers = []
scores = []

print("Playing Bulls & Cows with %i unique digits\n" % size)

while True:
    ans = choices[0]
    answers.append(ans)
    # print ("(Narrowed to %i possibilities)" % len(choices))
    """score = input("Guess %2i is %*s. Answer (Bulls, cows)? "
                  % (len(answers), size, ''.join(ans)))"""
    print("Guess %d is %s." % (len(answers), ans))
    score = score_giver(chosen_secret, ans)
    print("Player scores the guess as: %s" % (score,))
    # score = parse_score(score)
    scores.append(score)
    # print("Bulls: %i, Cows: %i" % score)
    found = score == (size, 0)
    if found:
        print("Ye-haw!")
        break
    choices.remove(ans)
    choices = [c for c in choices if score_giver(ans, c) == score]
    # print(choices)
    if not choices:
        print("Bad scoring? nothing fits those scores you gave:")
        print('  ' +
              '\n  '.join("%s -> %s" % (''.join(an), sc)
                          for an, sc in zip(answers, scores)))
        break

"""
code = code_maker(size)
print("Code chosen is - " + code)
"""

"""
guess = '0000'
print("Score for guess = %s is - %s" % (guess, (score_giver(code, guess),)))
guess = '1111'
print("Score for guess = %s is - %s" % (guess, (score_giver(code, guess),)))
guess = '2233'
print("Score for guess = %s is - %s" % (guess, (score_giver(code, guess),)))
guess = '4567'
print("Score for guess = %s is - %s" % (guess, (score_giver(code, guess),)))
guess = '8090'
print("Score for guess = %s is - %s" % (guess, (score_giver(code, guess),)))
guess = '2345'
print("Score for guess = %s is - %s" % (guess, (score_giver(code, guess),)))
guess = '2712'
print("Score for guess = %s is - %s" % (guess, (score_giver(code, guess),)))
guess = '3686'
print("Score for guess = %s is - %s" % (guess, (score_giver(code, guess),)))
"""
