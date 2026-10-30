# Stan początkowy laboratorium 3

Backend (`app/`, `pyproject.toml`, `uv.lock`) jest identyczny z katalogiem `solution/` laboratorium 2.

Nowy jest katalog `frontend/`:

| Plik | Zawartość |
|---|---|
| `index.html` | gotowy szkielet strony: formularz, lista, filtr, miejsca na komunikaty |
| `styles.css` | gotowy arkusz stylów |
| `js/main.js` | jedna linia wypisująca komunikat do konsoli |

HTML i CSS są dostarczane gotowe, ponieważ przedmiotem zajęć jest warstwa JavaScript i komunikacja z API, a nie projektowanie interfejsu. Jest to jedyne odstępstwo od zasady `solution/` poprzedniego laboratorium == `starter/` bieżącego.

## Kto czego potrzebuje

| Sytuacja | Co skopiować |
|---|---|
| własny projekt z laboratorium 2, z odpowiedzią 409 | tylko katalog `frontend/` |
| własny projekt bez odpowiedzi 409 | `frontend/` oraz `app/main.py` |
| brak projektu | cały katalog |

## Uruchomienie

Terminal 1:

```bash
uv sync
uv run fastapi dev app/main.py
```

Terminal 2:

```bash
uv run python -m http.server 5500 --bind 127.0.0.1 --directory frontend
```

Przeglądarka: `http://127.0.0.1:5500`. Bez konfiguracji CORS, którą studenci dodają w kroku 5 instrukcji, strona nie odczyta danych z API. Jest to stan zamierzony.
