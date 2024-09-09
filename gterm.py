#!.venv/bin/python
import typer
import data
from rich import print


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
def search(search: str = "") -> None:
    if not search:
        search = typer.prompt("Enter game to search for: ")

    result = data.search_rawg_api(search)
    print("result is type: ", type(result))
    print(result.json())


@app.command()
def clear_cache():
    data.clear_cache()


if __name__ == "__main__":
    app()
