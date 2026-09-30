"""
Spiellogik für WikiTrivia.

Schnittstelle für das Team:

    from game_logic.logic import play_game
    result = play_game(get_question)

get_question ist eine Funktion, die bei jedem Aufruf genau EINE neue Frage liefert
(oder None, wenn keine Frage mehr verfügbar ist):

    {
        "aussage": "Berlin ist die Hauptstadt Deutschlands.",
        "erfunden": False,              # False = wahr, True = erfunden
        "erklaerung": "..."             # optional
    }

Spielende / Rückgabewerte:

- WIN_SCORE richtige Antworten    -> "won"
- MAX_MISTAKES falsche Antworten  -> "lost"
- 3 ungültige Eingaben            -> "invalid_input"
- keine weitere Frage             -> "not_enough_questions"
"""

from awards import award_progress  # von Julia importiert

WIN_SCORE = 5       # so viele richtige Antworten zum Gewinnen
MAX_MISTAKES = 3    # so viele Fehler bis Game Over
MAX_INPUT_TRIES = 3


def ask_true_false(statement, erfunden, erklaerung=""):
    """Zeigt eine Aussage und gibt True bei richtiger Antwort zurück.

    Bei drei ungültigen Eingaben wird ein ValueError ausgelöst.
    Eine gültige, aber falsche Antwort gibt False zurück.
    """
    print("+----------------------------------------+")
    print(f"  {statement}")
    print("+----------------------------------------+")

    for attempt in range(1, MAX_INPUT_TRIES + 1):
        answer = input("  Your choice [T/F] > ").strip().casefold()

        if answer in ("t", "f"):
            break

        print(f"  [!] Please enter T or F. ({attempt}/{MAX_INPUT_TRIES})")
    else:
        # Läuft nur, wenn keine gültige Eingabe kam (Schleife ohne break beendet).
        raise ValueError("Entered an invalid answer three times.")

    # erfunden=True bedeutet: Die Aussage ist falsch, also ist F richtig.
    correct_answer = "f" if erfunden else "t"
    is_correct = answer == correct_answer

    if is_correct:
        print("  [OK] Correct! :)")
    else:
        print(f"  [X] Sorry, wrong. :( ")

    if erklaerung:
        print(f"  ℹ {erklaerung}")

    return is_correct


def play_game(get_question):
    """Spielt Runden, bis gewonnen/verloren ist, und gibt das Ergebnis zurück."""
    correct = 0
    mistakes = 0
    number = 0

    print("\n==========================================")
    print("       WIKITRIVIA - TRUE OR FALSE")
    print("==========================================")

    while correct < WIN_SCORE and mistakes < MAX_MISTAKES:
        number += 1
        question = get_question()

        if question is None:
            return "not_enough_questions"

        print(f"\n              ROUND {number}")
        print("------------------------------------------")

        try:
            is_correct = ask_true_false(
                question["aussage"],
                question["erfunden"],
                question.get("erklaerung", ""),
            )
        except ValueError as error:
            print(f"  [X] {error}")
            return "invalid_input"

        if is_correct:
            correct += 1
        else:
            mistakes += 1

        award_progress(correct, mistakes)
        print()

    # Die Schleife endet nur über eine der beiden Bedingungen:
    return "won" if correct >= WIN_SCORE else "lost"