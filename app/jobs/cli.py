import typer
from app.jobs.ai import hello_world

cli = typer.Typer()


@cli.command()
def print_hello_world():
    hello_world()


@cli.command()
def print_hello_world_again():
    hello_world()


if __name__ == "__main__":
    cli()
