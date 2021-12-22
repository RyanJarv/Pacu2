import subprocess

import typer
from . import keys, view

app = typer.Typer(help='help for aws command', short_help='aws cmd')
app.add_typer(keys.app, name='keys', help='help for keys command', short_help='keys cmd')
app.add_typer(view.app, name='view', help='help for keys command', short_help='keys cmd')


@app.command(help='help for whoami command', short_help='whoami cmd')
def whoami():
    subprocess.call(['aws', 'sts', 'get-caller-identity'])


if __name__ == "__main__":
    app()
