import typer
from .app import Game

app = typer.Typer(add_completion=False)


@app.command()
def play(low: int = 1, high: int = 100, tries: int = 7) -> None:
    """Starte das Zahlenraten-Spiel als CLI."""
    game = Game(low, high, tries)
    for _ in range(tries):
        try:
            value = int(typer.prompt(f"Rate eine Zahl zwischen {low} und {high}"))
        except Exception:
            typer.echo("Bitte eine ganze Zahl eingeben.")
            continue
        result = game.guess(value)
        if result == "correct":
            typer.echo("Gewonnen!")
            raise typer.Exit(code=0)
        hint = "Zu klein" if result == "higher" else "Zu groß"
        typer.echo(hint)
    typer.echo(f"Verloren! Die Zahl war {game.secret}")
    raise typer.Exit(code=1)


def main() -> None:
    app()


if __name__ == "__main__":
    main()