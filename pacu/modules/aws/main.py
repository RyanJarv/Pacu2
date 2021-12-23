import subprocess

import typer
from . import users

app = typer.Typer(help='help for aws command', short_help='aws cmd')
# app.add_typer(keys.app, name='keys', help='help for keys command', short_help='keys cmd')
# app.add_typer(view.app, name='view', help='help for view command', short_help='view cmd')
app.add_typer(users.app, name='users', help='help for users command', short_help='users cmd')


@app.command(help='help for whoami command', short_help='whoami cmd')
def whoami():
    subprocess.call(['aws', 'sts', 'get-caller-identity'])


if __name__ == "__main__":
    app()
