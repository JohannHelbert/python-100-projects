# Python 100 Projects (Monorepo)

Lernpfad mit 100 Projekten von leicht bis pro. Codespaces‑fertig, mit Tests, Linting, Typen und CI.

## Setup im Codespace
- Öffne "Code" → "Create codespace on main".
- Warte den Build ab (devcontainer).
- Danach im Terminal:
```bash
pre-commit install
pytest -q
guess  # CLI von Projekt 1 starten
```

## Struktur
- projects/p001_number_guess: Projekt 1 – Zahlenraten (CLI)
- projects/_template: Vorlage für neue Projekte
- tests/: Tests für Projekte

## Devtools
- Python 3.12, Ruff, Black, MyPy, pytest, pre-commit
- CI: Lint, Typen, Tests

## Nächste Schritte
- Projekt 1 durchspielen, dann Projekt 2 anlegen (via _template).