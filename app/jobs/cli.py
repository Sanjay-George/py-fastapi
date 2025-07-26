import typer
from app.jobs.ai import hello_world
from app.jobs.ingest_pdf import pdf

cli = typer.Typer()


@cli.command()
def print_hello_world():
    hello_world()


@cli.command()
def ingest_pdf():
    pdf()


if __name__ == "__main__":
    cli()
