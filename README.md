# bulls_and_cows
A python3 implementation of the famous bulls and cows game, precursor to Mastermind

    Source : https://www.python-course.eu/mastermind.php
    
The source code available at above URL works well for cases where the digits are not allowed to be duplicated 
in the secret code. 
However with my enhancements now, the code will work even if the digits are repeated.

Latest enhancement is a code-maker implementation which makes up a random secret code
and returns scores back to the code-breaker guesses.

Now one can specify the "secret size" and number of "trials to run" as input and the "average" and 
"full run-time" is computed at the end.
