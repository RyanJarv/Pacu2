import configparser
from typing import Optional

import typer

from pacu.config import Config
from pacu.aws import shared_credential_path

app = typer.Typer()


@app.command(help='help for use command', short_help='use cmd')
def use(selection: Optional[int] = typer.Argument(False)):
    profiles = get_profiles()

    if not selection:
        selection = typer.prompt("selection> ")

    p = list(profiles)[int(selection)]
    Config().profile = p

    print(f"Set current AWS profile to {p}")


@app.command(name='list', help='help for list command', short_help='list cmd')
def _list():
    print(f"*** {shared_credential_path()} ***")
    for i, profile in enumerate(get_profiles()):
        print(f"{i}) {profile}")


def get_profiles():
    config = configparser.ConfigParser()
    config.read(shared_credential_path())
    for profile in config.sections():
        yield profile


if __name__ == "__main__":
    app()
