#!.venv/bin/python
import typer
import data
from rich.console import Console as rConsole
from rich import print
from typing_extensions import Annotated


app = typer.Typer()


@app.command()
def news():
    pass


@app.command()
def price():
    pass


@app.command()
def stats():
    pass


@app.command()
def search(
    keyword: Annotated[
        str, typer.Argument(help="The name of the game your searching for")
    ] = "",
    clear_cache: Annotated[
        bool, typer.Option(help="Deletes cached search results")
    ] = False,
    raw_json: Annotated[
        bool, typer.Option(help="Displays raw json search results in terminal pager")
    ] = False,
) -> None:
    """
    Displays a list of games relevant to KEYWORD
    """

    if not keyword:
        keyword = typer.prompt("Enter game your searching for")

    if clear_cache:
        data.clear_cache()
        print("[bold red]Notice![/bold red] search cache has been cleared")
        return

    if raw_json:
        console = rConsole()
        with console.pager():
            console.print(data.search_rawg_api(keyword).json())
        return

    print(data.search_rawg_api(keyword).json())


if __name__ == "__main__":
    app()
