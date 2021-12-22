import configparser

import typer

from pacu.settings import profile_path
from pacu.utils import get_config_path

app = typer.Typer()


@app.command(help='help for use command', short_help='use cmd')
def use():
    _list()
    profiles = get_profiles()
    resp = typer.prompt("selection> ")
    profile = list(profiles)[int(resp)]
    profile_path.write_text(profile)


@app.command(name='list', help='help for list command', short_help='list cmd')
def _list():
    print(f"*** {get_config_path()} ***")
    for i, profile in enumerate(get_profiles()):
        print(f"{i}) {profile}")


def get_profiles():
    config = configparser.ConfigParser()
    config.read(get_config_path())
    for profile in config.sections():
        yield profile.removeprefix('profile ')


if __name__ == "__main__":
    app()
