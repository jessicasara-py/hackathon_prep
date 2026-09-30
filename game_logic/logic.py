"""
Spiellogik für WikiTrivia.

Aufgabe dieser Datei:
- Aussagen anzeigen
- Antworten T/F prüfen
- Richtige Antworten und Fehler zählen
- Fortschritt nach jeder Antwort anzeigen
- Nach 10 richtigen Antworten oder 3 Fehlern das Spiel beenden


Schnittstelle für das Team:

    play_game(get_question)

Import in main.py:

    from game_logic.logic import play_game


get_question ist eine Funktion, die immer genau EINE neue Frage liefert.

Eine Frage ist ein Dictionary und sieht zum Beispiel so aus:

    {
        "aussage": "Berlin ist die Hauptstadt Deutschlands.",
        "erfunden": False
    }


Bedeutung:

- "aussage":
    Der Text, der dem Spieler angezeigt wird.

- "erfunden":
    False = Aussage ist wahr
    True  = Aussage ist erfunden / falsch


Ablauf des Spiels:

1. play_game() fordert über get_question() eine Frage an.
2. Die Frage wird dem Spieler angezeigt.
3. Der Spieler antwortet mit T oder F.
4. Die Antwort wird geprüft.
5. Richtige Antworten oder Fehler werden gezählt.
6. Der Fortschritt wird angezeigt.
7. Nur wenn das Spiel weiterläuft, wird die nächste Frage angefordert.

Dadurch werden nicht alle Fragen vorher erzeugt.
Eine neue Wikipedia-/KI-Frage wird erst erstellt, wenn sie wirklich
für die nächste Runde benötigt wird.


Spielende:

- 10 richtige Antworten -> "won"
- 3 falsche Antworten  -> "lost"
- 3 ungültige Eingaben -> "invalid_input"
- keine weitere Frage   -> "not_enough_questions"


play_game() gibt einen dieser Strings an main.py zurück:

    "won"
    "lost"
    "invalid_input"
    "not_enough_questions"

main.py entscheidet anschließend, was angezeigt wird,
zum Beispiel Gewinner-ASCII oder Game-Over-ASCII.
"""

from awards import award_progress  # von Julia importiert

def ask_true_false(statement, erfunden):
    """Zeigt eine Aussage und gibt True bei richtiger Antwort zurück.

    Bei drei ungültigen Eingaben wird ein ValueError ausgelöst.
    Eine gültige, aber falsche Antwort gibt False zurück.
    """
    print("+----------------------------------------+")
    print(f"  {statement}")
    print("+----------------------------------------+")

    # Maximal drei Versuche für eine gültige Eingabe.
    for attempt in range(1, 4):
        answer = input("  Your Choice [T/F] > ").strip().casefold()

        if answer in ("t", "f"):
            break

        print(f"  [!] Please enter T oder F ein. ({attempt}/3)")
    else:
        # Dieser Teil läuft nur, wenn kein gültiges T oder F eingegeben wurde.
        raise ValueError("Entered an invalid answer three times.")

    # erfunden=True bedeutet: Die Aussage ist falsch und F ist richtig.
    correct_answer = "f" if erfunden else "t"

    if answer == correct_answer:
        print("  [OK] Correct! :)")
        return True

    print(f"  [X] Sorry wrong. :( Correct answer was: {correct_answer.upper()}")
    return False


def play_game(get_question):
    """Spielt die übergebenen Fragen durch und gibt das Spielergebnis zurück."""
    correct = 0
    mistakes = 0

    print("\n==========================================")
    print("       WIKITRIVIA - TRUE OR FALSE")
    print("==========================================")

    number = 0

    while correct < 10 and mistakes < 3:
        number += 1
        question = get_question()

        if question is None:
            return "not_enough_questions"

        statement = question["aussage"]
        erfunden = question["erfunden"]

        print(f"\n              ROUND {number}")
        print("------------------------------------------")

        try:
            is_correct = ask_true_false(statement, erfunden)
        except ValueError as error:
            # Drei ungültige Eingaben beenden das Spiel mit eigenem Ergebnis.
            # main.py kann dafür eine passende Meldung anzeigen.
            print(f"  [X] {error}")
            return "invalid_input"

        if is_correct:
            correct += 1
        else:
            mistakes += 1

        award_progress(correct, mistakes)   # geändert, sonst taucht es doppelt auf
        print()                             # bei award

        if mistakes == 3:
            # main.py kann hier das Game-Over-ASCII-Bild anzeigen.
            return "lost"

        if correct == 10:
            # main.py kann hier das Gewinnerbild und Trophäen anzeigen.
            return "won"
