#!.venv/bin/python
import typer
from rich.console import Console as rConsole
from rich import print
from typing_extensions import Annotated
import data


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
        paginate(data.query_rawg_api(keyword).json())

    search_results = data.query_rawg_api(keyword).json()
    print(data.transform(search_results))
    # replace print above with interactive interface
    # navigate search results, select game for more info, or request next page


def paginate(text):
    """
    Displays TEXT via terminal pager
    """
    console = rConsole()
    with console.pager():
        console.print(text)
    return


if __name__ == "__main__":
    app()
