#!.venv/bin/python
import typer
from rich.console import Console as rConsole
from rich import print
from typing_extensions import Annotated
import search
import ls
import data



app = typer.Typer()
app.add_typer(search.app, name="search")
app.add_typer(ls.app, name="list")


@app.command()
def news():
    pass


@app.command()
def price():
    pass


@app.command()
def stats():
    pass


if __name__ == "__main__":
    app()
