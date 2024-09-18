import typer
from rich.console import Console as rConsole
from rich import print
from typing_extensions import Annotated
from enum import Enum
import data

app = typer.Typer()


class Endpoint(Enum):
    """
    A Enum class representing a list of RAWG API endpoints
    """

    DEVELOPERS = "/developers"
    PUBLISHERS = "/publishers"
    GENRES = "/genres"
    STORES = "/stores"
    TAGS = "/tags"


@app.command()
def parent_platforms():
    """
    Display list of parent and respective children platforms
    """
    response = data.list_platforms(parent=True)
    main_platforms = response["results"]

    for main_platform in main_platforms:
        print(f"\nID:{main_platform['id']} - {main_platform['name']}")
        for platform in main_platform["platforms"]:
            print(f"\tID:{platform['id']} - {platform['name']}")


@app.command()
def details(id: int, endpoint: str):
    """
    Display details on ID from ENDPOINT
    """
    pass


@app.command()
def developers(page_size: Annotated[int, typer.Option(help="Items per page")] = 10):
    """Display list of developers"""
    response = data.list_endpoint(Endpoint.DEVELOPERS.value)
    print(response)


@app.command()
def publishers(page_size: Annotated[int, typer.Option(help="Items per page")] = 10):
    """Display list of publishers"""
    response = data.list_endpoint(Endpoint.PUBLISHERS.value)
    print(response)


@app.command()
def genres(page_size: Annotated[int, typer.Option(help="Items per page")] = 10):
    """Display list of genres"""
    response = data.list_endpoint(Endpoint.GENRES.value)
    print(response)


@app.command()
def stores(page_size: Annotated[int, typer.Option(help="Items per page")] = 10):
    """Display list of developers"""
    response = data.list_endpoint(Endpoint.STORES.value)
    print(response)


@app.command()
def tags(page_size: Annotated[int, typer.Option(help="Items per page")] = 10):
    """Display list of developers"""
    response = data.list_endpoint(Endpoint.TAGS.value)
    print(response)


if __name__ == "__main__":
    app()
