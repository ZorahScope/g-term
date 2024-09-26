import typer
from rich.console import Console as rConsole
from rich import print
from typing_extensions import Annotated
from typing import List
from models import Game
import data

app = typer.Typer()


@app.command()
def game(
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
        paginate(data.search_games(keyword))

    search_results = data.search_games(keyword)
    games = data.transform(search_results)
    display_games(games)
    # replace print above with interactive interface
    # navigate search results, select game for more info, or request next page


def display_games(games: List[Game]):
    for game in games:
        display = ""
        display += f"Name: {game.name.title()}\n"
        if not game.tba:
            display += f"Released: {game.released}\n"
        else:
            display += f"TBA: {game.tba}\n"
        genres = []
        for genre in game.genres:
            genres.append(genre["name"])
        display += f"Genres: {generate_list_str(genres)}\n"
        platforms = []
        for platform in game.platforms:
            platforms.append(platform["platform"]["name"])
        display += f"Platforms: {generate_list_str(platforms)}\n"
        display += f"ESRB: {game.esrb_rating['name'] if game.esrb_rating else None}\n"
        display += f"Metacritic: {game.metacritic}\n"

        print(f"\n{display}")


def generate_list_str(items: List[str]) -> str:
    result = ""
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f"{items[0]} and {items[1]}"
    for idx, item in enumerate(items):
        if idx > 0:
            result += ", "
        if idx == len(items) - 1:
            result += "and "
        result += item
    return result


def filter():
    pass


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
