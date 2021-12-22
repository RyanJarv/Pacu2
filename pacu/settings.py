import os
from pathlib import Path

import typer

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

app_dir = Path(typer.get_app_dir('pacu'))
profile_path = app_dir/'profile'
