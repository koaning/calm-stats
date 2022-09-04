import typer 
from pathlib import Path
import pandas as pd


def stack(new: Path, old: Path):
    """
    Stack new csv data on to some old one. 
    """
    pd.concat([pd.read_csv(new), pd.read_csv(old)]).to_csv(old)



typer.run(stack)
