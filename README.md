<p align="center">
  <img src="wiki_tricky_characters.jpg" alt="WikiTricky" width="800">
</p>

# WikiTricky

A console-based trivia game powered by the Wikipedia API. Created during the **MSIT Hackathon** (topic: Wikipedia).

The player chooses a category. The game retrieves a random Wikipedia article, and an AI generates a statement based on the article that is either **true or made up**. The player has to guess whether the statement is correct.

---

## Game Flow

1. **Game menu**: Enter a name and start the game
2. **Choose a category**: Select a category from the available list
3. **API call**: Retrieve a random Wikipedia article from the selected category (optional: only articles with at least X page views)
4. **AI-generated statement**: Generate a statement based on the article content:

   ```json
   { "aussage": "...", "erfunden": true }
   ```
5. **User input**: The player answers with `W` (true) or `F` (false)
6. **Input validation**: Invalid input can be entered up to 3 times
7. **Evaluation**: :) or :( with the current score
8. **Trophies**: Awards for special achievements

---

## Requirements

* Python 3.10+
* Internet connection (Wikipedia API)

## Installation

```bash
# Clone the repository
git clone <repo-url>
cd <project-folder>

# Create a virtual environment (recommended)
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# Install dependencies
# requests is used to check Wikipedia page views
pip3 install wikipedia-api python-dotenv requests rich openai
```

## Configuration

Configuration is stored in a `.env` file in the project root. It is **not committed to the repository**.

```bash
cp .env-dist .env
```

Then configure the `.env` file:

```env
WIKI_APP_NAME=WikiTricky
WIKI_CONTACT=https://github.com/<user>/<repo>
WIKI_LANGUAGE=de
```

| Variable        | Description                                                     | Required |
| --------------- | --------------------------------------------------------------- | -------- |
| `WIKI_APP_NAME` | Application name used in the User-Agent                         | No       |
| `WIKI_CONTACT`  | Contact information for Wikimedia (email **or** repository URL) | **Yes**  |
| `WIKI_LANGUAGE` | Wikipedia language edition (`de`, `en`, ...)                    | No       |

> **Why is a contact required?** Wikimedia requires API requests to include a User-Agent with contact information. Without it, requests may be throttled or blocked. A GitHub repository URL is sufficient; a private email address is not required.

## Running the Game

Always start the game from the **project root** using `main.py`:

```bash
python main.py
```

Do not run files from the subdirectories directly, as this can cause import errors (`ModuleNotFoundError`).

---

## Project Structure

```text
.
├── ai_calls/                     # AI: generate true/false statements from article text
│   └── __init__.py
├── api_calls/                    # Wikipedia API
│   ├── __init__.py
│   ├── wiki_client.py            # Central client: get_wiki()
│   ├── wikipedia_check_category.py
│   └── wikipedia_get_page.py
├── game_logic/                   # Game flow, input validation, scoring
│   └── __init__.py
├── menues/                       # Console menus (main menu, categories)
│   └── __init__.py
├── awards.py                     # Trophies and progress display
├── main.py                       # Entry point
├── .env                          # Local configuration (not committed)
├── .env-dist                     # .env template
├── .gitignore
├── pyproject.toml
└── README.md
```

> **Naming convention:** Use underscores (`api_calls`) instead of hyphens (`api-calls`) for directories and files. Python cannot import module names containing hyphens.

---

## Using the Wikipedia Client

The client is created centrally in `api_calls/wiki_client.py` and instantiated only once. All other modules access it through `get_wiki()`:

```python
from api_calls.wiki_client import get_wiki

page = get_wiki().page("Augsburg")

if page.exists():
    print(page.title)
    print(page.summary[:200])
```

We use the **synchronous client** (`wikipediaapi.Wikipedia`): each request waits for the response before the code continues. This makes the code easier to understand and debug.

If performance becomes an issue, the client can later be switched to `wikipediaapi.AsyncWikipedia`. Only `wiki_client.py` would need to be modified.

---

## Open Points / Ideas

* [ ] Category list and validation of valid categories
* [ ] Retrieve a random article from a category
* [ ] Filter: only articles with at least X page views (Wikimedia Pageviews API)
* [ ] AI integration for generating true/false statements in JSON format
* [ ] Error handling: invalid API responses, exceptions, missing pages
* [ ] Score and player name
* [ ] Trophies
* [ ] Console eye candy (colors, ASCII art)
* [ ] *Optional:* GUI

---

## Links

* [Wikipedia API (Python package)](https://pypi.org/project/Wikipedia-API/)
* [Wikimedia User-Agent Policy](https://meta.wikimedia.org/wiki/User-Agent_policy)
* [Wikimedia REST API](https://en.wikipedia.org/api/rest_v1/)


