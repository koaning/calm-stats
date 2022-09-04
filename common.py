import typer 
from pathlib import Path
import pandas as pd


app = typer.Typer(name="common", add_completion=False, help="Small app with utilities.")


@app.command("version")
def version():
    """Shows a version."""
    return "0.1.0"

@app.command("stack")
def stack(new: Path, old: Path):
    """Stack new csv data on to some old one. """
    pd.concat([pd.read_csv(new), pd.read_csv(old)]).to_csv(old)


if __name__ == "__main__":
    app()
