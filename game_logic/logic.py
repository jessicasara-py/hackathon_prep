def ask_true_false(statement, is_true):
    print("+----------------------------------------+")
    print(f"  {statement}")
    print("+----------------------------------------+")

    while True:
        answer = input("  Deine Wahl [W/F] > ").strip().casefold()

        if answer in ("w", "f"):
            break

        print("  [!] Bitte gib W oder F ein.")

    correct_answer = "w" if is_true else "f"

    if answer == correct_answer:
        print("  [OK] Richtig!")
        return True

    print(f"  [X] Leider falsch. Richtig war: {correct_answer.upper()}")
    return False


def play_game(questions):
    # questions ist eine Liste von Aussagen mit der jeweiligen Lösung.
    # Diese Liste kommt später aus dem Wikipedia-Teil.
    correct = 0
    mistakes = 0

    print("\n==========================================")
    print("       WIKIPEDIA - WAHR ODER FALSCH")
    print("==========================================")

    for number, (statement, is_true) in enumerate(questions, start=1):
        print(f"\n              RUNDE {number}")
        print("------------------------------------------")

        if ask_true_false(statement, is_true):
            correct += 1
        else:
            mistakes += 1

        print("------------------------------------------")
        print(f"  RICHTIG: {correct}/10    FEHLER: {mistakes}/3")
        print("------------------------------------------")

        if mistakes == 3:
            # "lost" wird an main.py zurückgegeben.
            # Dort kann das traurige ASCII-Bild aufgerufen werden.
            return "lost"

        if correct == 10:
            # "won" wird an main.py zurückgegeben.
            # Dort kann das Gewinner-ASCII aus awards.py aufgerufen werden.
            return "won"

    # Wird erreicht, wenn die Fragen ausgehen, bevor das Spiel entschieden ist.
    return "not_enough_questions"


if __name__ == "__main__":
    # Nur zum Testen. Später kommen die Fragen aus dem Wikipedia-Teil.
    test_questions = [
        ("Berlin ist die Hauptstadt von Deutschland.", True),
        ("Die Erde hat zwei Monde.", False),
        ("Paris liegt in Italien.", False),
    ]

    result = play_game(test_questions)
    print(f"\nTestergebnis: {result}")

# Später in main.py verwenden:
# from logic import play_game
