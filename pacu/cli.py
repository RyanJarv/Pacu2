import os

import typer

from pacu.pacu import PacuRepl

from pacu.settings import profile_path, app_dir
from pacu.utils import set_profile_env


def callback():
    if profile_path.is_file():
        set_profile_env(profile_path.read_text())
    elif not app_dir.is_dir():
        os.makedirs(app_dir, exist_ok=True)


app = typer.Typer(callback=callback)

pacu = PacuRepl()
pacu.load_modules(app)


@app.command('repl')
def repl():
    pacu.repl()



if __name__ == '__main__':
    app(prog_name="pacu")

