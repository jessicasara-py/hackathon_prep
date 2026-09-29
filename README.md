
# WikiTrivia

Ein Konsolen-Quizspiel auf Basis der Wikipedia-API. Entstanden beim **MSIT Hackathon** (Thema: Wikipedia).

Der Spieler wählt eine Kategorie. Das Spiel holt einen zufälligen Wikipedia-Artikel, und eine KI erzeugt daraus eine Aussage, die **wahr oder erfunden** ist. Der Spieler muss erraten, ob die Aussage stimmt.

---

## Spielablauf

1. **Spielmenü**: Name eingeben, Spiel starten
2. **Kategorie wählen**: Liste mit Kategorien, der Spieler wählt eine aus
3. **API-Call**: zufälliger Wikipedia-Artikel aus der Kategorie (optional: nur Artikel mit mindestens X Aufrufen)
4. **KI-Aussage**: Aus dem Artikelinhalt wird eine Aussage generiert:
   ```json
   { "aussage": "…", "erfunden": true }
   ```
5. **User-Input**: Der Spieler antwortet mit `W` (wahr) oder `F` (falsch)
6. **Eingabe prüfen**: Bei ungültiger Eingabe wird bis zu 3-mal nachgefragt
7. **Auswertung**: :) oder :( mit Punktestand
8. **Trophäen**: Auszeichnungen für besondere Leistungen

---

## Voraussetzungen

- Python 3.10+
- Internetzugang (Wikipedia-API)

## Installation

```bash
# Repository klonen
git clone <repo-url>
cd <projektordner>

# Virtuelle Umgebung anlegen (empfohlen)
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# Abhängigkeiten installieren
# request für check der Seitenaufrufe eine Wiki - Seite
pip3 install wikipedia-api python-dotenv requests
```

## Konfiguration

Die Konfiguration liegt in einer `.env`-Datei im Projekt-Root. Sie wird **nicht** ins Repository eingecheckt.

```bash
cp .env-dist .env
```

Danach die `.env` anpassen:

```env
WIKI_APP_NAME=WikiTrivia
WIKI_CONTACT=https://github.com/<user>/<repo>
WIKI_LANGUAGE=de
```

| Variable        | Bedeutung                                                 | Pflicht |
|-----------------|-----------------------------------------------------------|---------|
| `WIKI_APP_NAME` | Name der App im User-Agent                                | nein    |
| `WIKI_CONTACT`  | Kontakt für Wikimedia (E-Mail **oder** Repo-URL)          | **ja**  |
| `WIKI_LANGUAGE` | Sprachversion der Wikipedia (`de`, `en`, …)               | nein    |

> **Warum ein Kontakt?** Wikimedia verlangt bei jeder API-Anfrage einen User-Agent mit Kontaktmöglichkeit. Fehlt er, werden Anfragen gedrosselt oder blockiert. Eine GitHub-Repo-URL reicht aus, eine private E-Mail ist nicht nötig.

## Starten

Immer aus dem **Projekt-Root** über `main.py` starten:

```bash
python main.py
```

Dateien aus den Unterordnern nicht direkt ausführen, sonst schlagen die Imports fehl (`ModuleNotFoundError`).

---

## Projektstruktur

```
.
├── ai_calls/                     # KI: Aussagen (W/F) aus Artikeltext generieren
│   └── __init__.py
├── api_calls/                    # Wikipedia-API
│   ├── __init__.py
│   ├── wiki_client.py            # zentraler Client: get_wiki()
│   ├── wikipedia_check_category.py
│   └── wikipedia_get_page.py
├── game_logic/                   # Spielablauf, Eingabe prüfen, Punkte
│   └── __init__.py
├── menues/                       # Konsolen-Menüs (Hauptmenü, Kategorien)
│   └── __init__.py
├── awards.py                     # Trophäen
├── main.py                       # Einstiegspunkt
├── .env                          # lokale Konfiguration (nicht im Repo)
├── .env-dist                     # Vorlage für .env
├── .gitignore
├── pyproject.toml
└── README.md
```

> **Namenskonvention:** Ordner und Dateien mit Unterstrich (`api_calls`) statt Bindestrich (`api-calls`). Python kann Namen mit Bindestrich nicht importieren.

---

## Wikipedia-Client verwenden

Der Client wird zentral in `api_calls/wiki_client.py` erzeugt und nur einmal instanziiert. Alle anderen Module holen ihn über `get_wiki()`:

```python
from api_calls.wiki_client import get_wiki

page = get_wiki().page("Augsburg")
if page.exists():
    print(page.title)
    print(page.summary[:200])
```

Wir nutzen den **synchronen Client** (`wikipediaapi.Wikipedia`): Jede Anfrage wartet auf die Antwort, bevor der Code weiterläuft. Das ist einfach zu verstehen und zu debuggen. Bei Performance-Problemen lässt sich später auf `wikipediaapi.AsyncWikipedia` umstellen. Dafür muss nur `wiki_client.py` angepasst werden.

---

## Offene Punkte / Ideen

- [ ] Kategorienliste und Validierung gültiger Kategorien
- [ ] Zufälliger Artikel aus einer Kategorie
- [ ] Filter: nur Artikel mit mindestens X Aufrufen (Wikimedia Pageviews API)
- [ ] KI-Anbindung für Aussagen (W/F) im JSON-Format
- [ ] Fehlerbehandlung: ungültige API-Antworten, Exceptions, fehlende Seiten
- [ ] Punktestand und Spielername
- [ ] Trophäen
- [ ] Eye Candy in der Konsole (Farben, ASCII-Art)
- [ ] *Optional:* GUI

---

## Links

- [Wikipedia-API (Python-Paket)](https://pypi.org/project/Wikipedia-API/)
- [Wikimedia User-Agent Policy](https://meta.wikimedia.org/wiki/User-Agent_policy)
- [Wikimedia REST API](https://en.wikipedia.org/api/rest_v1/)

