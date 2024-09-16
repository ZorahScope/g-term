import typer
from rich.console import Console as rConsole
from rich import print
from typing_extensions import Annotated
import search
import data

app = typer.Typer()


@app.command()
def parent_platforms():
    response = data.list_parent_platforms()
    print(response)


@app.command()
def platforms():
    pass


@app.command()
def platform_details():
    pass


@app.command()
def publisher():
    pass


@app.command()
def publisher_details():
    pass


if __name__ == "__main__":
    app()
