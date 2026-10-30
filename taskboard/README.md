# TaskBoard

System zarzadzania projektami i zadaniami rozwijany na laboratoriach przedmiotu
Podstawy programowania aplikacji webowych.

## Uruchomienie

API:

```bash
uv sync
uv run fastapi dev app/main.py
```

Frontend, w drugim terminalu:

```bash
uv run python -m http.server 5500 --bind 127.0.0.1 --directory frontend
```

API: http://127.0.0.1:8000, frontend: http://127.0.0.1:5500

## Endpointy

| Metoda | Sciezka | Status | Opis |
|---|---|---|---|
| GET | `/` | 200 | odpowiedz powitalna |
| GET | `/health` | 200 | status aplikacji |
| GET | `/tasks` | 200 | lista zadan, parametry `status` oraz `limit` |
| GET | `/tasks/{task_id}` | 200, 404 | pojedyncze zadanie |
| POST | `/tasks` | 201, 409, 422 | utworzenie zadania |
| PUT | `/tasks/{task_id}` | 200, 404 | zastapienie zadania |
| DELETE | `/tasks/{task_id}` | 204, 404 | usuniecie zadania |
| GET | `/docs` | 200 | dokumentacja OpenAPI |

## Stan projektu

Poczatek laboratorium 3: API z laboratorium 2 oraz szkielet frontendu w `frontend/`.

Dane sa przechowywane w pamieci procesu i znikaja po restarcie serwera.
Trwalosc danych zostanie dodana na zajeciach 6.
