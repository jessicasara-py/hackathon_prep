"""
Spiellogik für WikiTrivia.

Aufgabe dieser Datei:
- Aussagen anzeigen, hier sind gerade nur Bsp. zum testen
- Antworten W/F prüfen, können auch andere Zeichen benutzen
- Richtige Antworten und Fehler zählen
- Nach 10 richtigen Antworten oder 3 Fehlern das Spiel beenden

Schnittstelle für das Team:
    play_game(questions) für die main...
    in die main importieren >>> from game_logic.logic import play_game

questions muss eine Liste von Dictionaries sein, zum Beispiel:
    [
        {"aussage": "Berlin ist die Hauptstadt Deutschlands.", "erfunden": False},
        {"aussage": "Die Erde hat zwei Monde.", "erfunden": True},
    ]

Der KI-Teil liefert für jede Frage:
- "aussage": den Text, der dem Spieler angezeigt wird
- "erfunden": True, wenn die Aussage falsch ist; sonst False

play_game() gibt einen dieser Strings an main.py zurück:
- "won": 10 richtige Antworten erreicht >>>ASCII im main
- "lost": 3 falsche Antworten erreicht >>>ASCII im main
- "invalid_input": dreimal hintereinander keine gültige Eingabe
- "not_enough_questions": Die Fragen sind aufgebraucht

___________________________________________________________________

BSP.: für den main Teil:
from game_logic.logic import play_game

# Hier die Fragen aus dem Wikipedia- und KI-Teil sammeln.
# Jede Frage braucht genau die Schlüssel "aussage" und "erfunden".
questions = [
    {"aussage": "Berlin ist die Hauptstadt Deutschlands.", "erfunden": False}
]

result = play_game(questions)

if result == "won":
    print("Gewonnen!")  # Hier Gewinner-ASCII und Trophäen einfügen.
elif result == "lost":
    print("Game Over!")  # Hier Game-Over-ASCII einfügen.
elif result == "invalid_input":
    print("Spiel wegen ungültiger Eingaben beendet.")
elif result == "not_enough_questions":
    print("Es sind keine weiteren Fragen verfügbar.")
"""

from awards import award_progress  # von Julia importiert

def ask_true_false(statement, erfunden, erklaerung=""):
    """Zeigt eine Aussage und gibt True bei richtiger Antwort zurück.

    Bei drei ungültigen Eingaben wird ein ValueError ausgelöst.
    Eine gültige, aber falsche Antwort gibt False zurück.
    """
    print("+----------------------------------------+")
    print(f"  {statement}")
    print("+----------------------------------------+")

    # Maximal drei Versuche für eine gültige Eingabe.
    for attempt in range(1, 4):
        answer = input("  Deine Wahl [W/F] > ").strip().casefold()

        if answer in ("w", "f"):
            break

        print(f"  [!] Bitte gib W oder F ein. ({attempt}/3)")
    else:
        # Dieser Teil läuft nur, wenn kein gültiges W oder F eingegeben wurde.
        raise ValueError("Dreimal eine ungültige Antwort eingegeben.")

    # erfunden=True bedeutet: Die Aussage ist falsch und F ist richtig.
    correct_answer = "f" if erfunden else "w"
    is_correct = answer == correct_answer

    if is_correct:
        print("  [OK] Richtig! :)")
    else:
        print(f"  [X] Leider falsch. :( Richtig war: ")

    # NEU: Erklärung in beiden Fällen anzeigen (falls vorhanden)
    if erklaerung:
        print(f"  ℹ {erklaerung}")

    return is_correct


def play_game(questions):
    """Spielt die übergebenen Fragen durch und gibt das Spielergebnis zurück."""
    correct = 0
    mistakes = 0

    print("\n==========================================")
    print("       WIKITRIVIA - WAHR ODER FALSCH")
    print("==========================================")

    for number, question in enumerate(questions, start=1):
        # Diese Schlüssel müssen mit dem Ergebnis des KI-Teils übereinstimmen.
        statement = question["aussage"]
        erfunden = question["erfunden"]

        print(f"\n              RUNDE {number}")
        print("------------------------------------------")

        try:
            is_correct = ask_true_false(question["aussage"], question["erfunden"], question.get("erklaerung", ""))
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

    # Der Fragen-Generator hat zu wenige Fragen geliefert. kann dann später weggelassen werden
    return "not_enough_questions"


if __name__ == "__main__":
    # Lokaler Test dieser Datei. Dieser Teil läuft NICHT beim Import in main.py.
    test_questions = [
        {"aussage": "Berlin ist die Hauptstadt Deutschlands.", "erfunden": False},
        {"aussage": "Die Erde hat zwei Monde.", "erfunden": True},
        {"aussage": "Paris liegt in Italien.", "erfunden": True},
    ]

    result = play_game(test_questions)
    print(f"\nTestergebnis: {result}")
