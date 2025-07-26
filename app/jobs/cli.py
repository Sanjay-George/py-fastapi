import typer
from app.jobs.ai import run_batch_job, run_batch_job2

cli = typer.Typer()


@cli.command()
def batch():
    run_batch_job()


@cli.command()
def batch2():
    run_batch_job2()


if __name__ == "__main__":
    cli()
