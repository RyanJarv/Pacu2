import typer


def main(name: str = 'test'):
    typer.echo(f"Hello {name}")
