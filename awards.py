def award_progress(correct_answers, failed_attempts):
    goal = 10
    max_failed_attempts = 3
    GREEN = "\x1b[32m"
    RED = "\x1b[31m"
    WHITE = "\x1b[37m"
    RESET = "\x1b[0m"

    print("\n**** YOUR QUIZ PROGRESS ****")
    print("-" * 28)

    # Correct answers
    for position in range(1, goal + 1):
        if position <= correct_answers:
            print(f"{GREEN}●{RESET}", end=" ")
        else:
            print("○", end=" ")

    print("||", end=" ")

    # Failed attempts
    for position in range(1, max_failed_attempts + 1):
        if position > max_failed_attempts - failed_attempts:
            print(f"{RED}x{RESET}", end=" ")
        else:
            print(f"{WHITE}x{RESET}", end=" ")



