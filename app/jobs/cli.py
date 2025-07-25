import typer
from app.jobs.ai import run_batch_job

cli = typer.Typer()


@cli.command()
def batch():
    run_batch_job()


if __name__ == "__main__":
    cli()
