# *********************** #
# @UTHOR: AKSHAY NEHE     #
# Date : 17-Apr-2019      #
# *********************** #
import time
from itertools import product
from random import choice
from random import shuffle

# Valid digits
symbols = '0123456789'
# Size of secret
# size = 4
size = int(input("What is the string size to play for? "))
# Number of trials to run
trials_count = int(input("How many trials do you want to run? "))

# Capturing start of time after size input
program_start = time.time()
guess_count = 0


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


def code_maker(code_size, symbols):
    """Manufactures the secret of specified size using given symbols

            Parameters:
            code_size (int): Size of secret code
            symbols (str): Valid symbols to make up the guess

            Returns:
            secret_code(str): Returning the secret code

    """
    secret_code = ''.join(choice(symbols) for i in range(code_size))
    return secret_code


def five_digs_or_less_breaker(pruned_symbols):
    # for t in range(trials_count):
    choices = [p for p in product(pruned_symbols, repeat=size)]
    shuffle(choices)
    answers = []
    scores = []

    print("Playing Bulls & Cows with %i digits\n" % size)

    while True:
        loop_start = time.time()
        ans = choices[0]
        answers.append(ans)
        # print ("(Narrowed to %i possibilities)" % len(choices))

        print("Guess %d is %s." % (len(answers), ans))
        score = score_giver(chosen_secret, ans)
        print("Player scores the guess as: %s" % (score,))
        # score = parse_score(score)
        scores.append(score)
        # print("Bulls: %i, Cows: %i" % score)
        code_found = score == (size, 0)
        if code_found:
            print("Ye-haw!")
            break
        choices.remove(ans)
        choices = [c for c in choices if score_giver(ans, c) == score]
        loop_end = time.time()
        print('Processed loop in: %s \n' % str(loop_end - loop_start))
        # print(choices)
        if not choices:
            print("Bad scoring? nothing fits those scores you gave:")
            print('\n'.join("%s -> %s" % (''.join(an), sc) for an, sc in zip(answers, scores)))
            break
    return ans, len(answers)


print("Playing for secret of size = %d" % size)

if size < 6:
    for t in range(trials_count):
        chosen_secret = code_maker(size, symbols)
        print("Chosen secret : %s" % chosen_secret)
        trial_start = time.time()
        guess_details = five_digs_or_less_breaker(symbols)
        guess_count += guess_details[1]
        trial_end = time.time()
        print("=== Trial complete in %s" % str(trial_end-trial_start))
else:
    found = None
    for t in range(trials_count):
        chosen_secret = code_maker(size, symbols)
        print("Chosen secret : %s" % chosen_secret)
        digits = [str(digit) for digit in range(10)]
        trial_start = time.time()
        initial_guesses = [[digit] * 10 for digit in range(10)]
        # shuffle(initial_guesses)
        hit_count = 0
        for guess in initial_guesses:
            score = score_giver(chosen_secret, guess)
            print("Player scores the guess as: %s" % (score,))
            found = score == (size, 0)
            if found:
                print("Ye-haw!")
                break
            if score == (0, 0):
                digits.remove(str(guess[0]))
                hit_count += 1

            if hit_count > 5:
                break

        if not found:
            guess_details = five_digs_or_less_breaker(''.join(digits))
            guess_count += guess_details[1]

        print("=== Trial complete ==== \n")
        trial_end = time.time()
        print("=== Trial complete in %s" % str(trial_end-trial_start))


# Capturing end of program
program_end = time.time()
print('Program run-time in seconds is: %s' % str(program_end - program_start))
print('Average number of guesses is: %s' % str(guess_count / trials_count))
print('Average trial run-time in seconds is: %s' % str((program_end - program_start) / trials_count))
print("***DISCLAIMER*** : For secrets of length more than 5, add 10 to displayed avg guess size above")

"""
code = code_maker(size)
print("Code chosen is - " + code)

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
