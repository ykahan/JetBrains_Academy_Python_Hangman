import random
import re
playing = True
while playing:
    print("H A N G M A N")
    play_or_exit_chosen = False
    while play_or_exit_chosen == False:
        play_or_exit = input('Type "play" to play the game, "exit" to quit:')
        if play_or_exit == "play" or play_or_exit == "exit":
            play_or_exit_chosen = True
    if play_or_exit == "exit":
            playing = False
            break

    print()

    words = ["python", "java", "kotlin", "javascript"]
    tries_left = 8
    solution = random.choice(words)
    length = len(solution)

    hyphens = "-" * length
    hint = hyphens
    already_guessed = list()
    lower_case_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                          'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                          'w', 'x', 'y', 'z']

    while tries_left > 0:
        print()
        print(hint)
        guess = input("Input a letter:")

        if len(guess) > 1 or len(guess) < 1:
            print("You should input a single letter")
            continue
        if guess not in lower_case_letters:
            print("Please enter a lowercase English letter")
            continue
        if guess not in solution:
            print("That letter doesn't appear in the word")
            if guess not in already_guessed:
                tries_left -= 1
        if guess in already_guessed:
            print("You've already guessed this letter")
        if guess in solution and guess not in already_guessed:
            instances = re.finditer(guess, solution)
            for instance in instances:
                hint = hint[0:instance.start()] + guess + hint[instance.start() + 1:]
            if hint == solution:
                break
        if len(guess) == 1 and guess in lower_case_letters:
            already_guessed.append(guess)

    if hint == solution:
        print("You guessed the word!")
        print("You survived!")
    else:
        print("You lost!")
