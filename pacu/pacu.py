import functools
import typer
import json
import importlib
from builtins import enumerate

import click
import itertools
import os
import shlex
import textwrap
from pathlib import Path
from types import ModuleType
from typing import Dict, Optional, List

from typing_extensions import get_type_hints
from prompt_toolkit import PromptSession
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.history import FileHistory
from prompt_toolkit.shortcuts import CompleteStyle, set_title
from prompt_toolkit.styles import Style

# from pacu import settings
from pacu.config import Config

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

app_dir = Path(typer.get_app_dir('pacu'))
profile_path = app_dir / 'profile'


class Pacu:
    def __init__(self):
        self.modules: Dict[str, ModuleType] = self.get_modules()

    @staticmethod
    def get_modules() -> Dict[str, ModuleType]:
        modules = {}
        for path in Path(ROOT_DIR).glob(
                os.path.join('modules', '*', 'main.py')
        ):
            rel = path.relative_to(ROOT_DIR)
            name = rel.parts[-2]
            mod_name = '.'.join(rel.parts)
            modules[name] = importlib.import_module(
                f"pacu.{mod_name.removesuffix('.py')}"
            )
        return modules

    def load_modules(self, app: 'typer.Typer'):
        """Check if app object exists and fallback to looking for the main function.

        The app method allows more customizations as well as multiple commands while the
         second, importing the main function is very simple. Below is an example of the
         later. See the typer docs for more details.

             import typer

             def main(name: str = 'test'):
                 typer.echo(f"Hello {name}")
        """

        for name, mod in self.modules.items():
            if getattr(mod, "main", False):
                app.command(
                    name=name,
                    help=getattr(mod, "help", ''),
                    short_help=getattr(mod, "short_help", ''),
                )(mod.main)  # type: ignore[attr-defined]
            elif getattr(mod, "app", False):
                app.add_typer(
                    mod.app,
                    name=name,
                    help=mod.app.info.help,
                    short_help=mod.app.info.short_help,
                )  # type: ignore[attr-defined]
            else:
                print(f"[WARN] No main or app attribute found for module {mod.__name__}")


class PacuRepl(Pacu):
    def __init__(self):
        super().__init__()

        set_title("Pacu")

        self.app: 'typer.Typer' = typer.Typer(add_completion=False)

        self.style = Style.from_dict(
            {
                'completion-menu.completion': 'bg:#008888 #ffffff',
                'completion-menu.completion.current': 'bg:#00aaaa #000000',
                'scrollbar.background': 'bg:#88aaaa',
                'scrollbar.button': 'bg:#222222',
            }
        )
        completion = list(self.modules.keys())
        completion.extend(['help', 'ls'])
        self.history = FileHistory(os.path.expanduser("~/.pacu_history"))
        self.session: 'PromptSession' = PromptSession(
            history=self.history,
            auto_suggest=AutoSuggestFromHistory(),
            enable_history_search=True,
            completer=WordCompleter(completion  , ignore_case=True),
            complete_style=CompleteStyle.READLINE_LIKE,
            style=self.style,
        )

        self._builtins = {
            "help": functools.partial(_help, self.app),
            "ls": functools.partial(_help, self.app),
            "config": _config,
        }

    def repl(self):
        self.load_modules(self.app)

        while True:
            try:
                cmd: str = shlex.split(self.session.prompt('> '))
                run = typer.main.get_command(self.app)

                try:
                    self._builtins[cmd[0]](cmd[1:])
                    continue
                except KeyError:
                    pass

                try:
                    run.main(cmd, standalone_mode=False)
                except Exception as e:  # pylint: disable=broad-except
                    print(e)
            except KeyboardInterrupt:
                pass


def _config(args: List[str]):
    conf = Config()
    try:
        print(conf.cmd(args))
    except AttributeError as e:
        print(e)


def _help(app: 'typer.Typer', args: List[str]):
    click_cmd = typer.main.get_command(app)
    ctx = click.Context(click_cmd)

    for i, arg in enumerate(args):
        if not getattr(click_cmd, "get_command", False):
            typer.echo("\n\n" + typer.style("Error:", fg=typer.colors.RED, bold=True) + \
                       f": Command '{' '.join(args[:i])}' does not have any subcommand named '{arg}'.\n\n")
            break

        click_cmd = click_cmd.get_command(ctx, arg)
        if not click_cmd:
            typer.echo(typer.style("Error:", fg=typer.colors.RED, bold=True) + \
                       f": No command named '{arg}' was found registered with pacu.")
            return

        ctx = click.Context(click_cmd)

    print(ctx.get_help())

