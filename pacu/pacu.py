import importlib
import os
import shlex
from pathlib import Path
from types import ModuleType
from typing import Dict

import typer
from prompt_toolkit import PromptSession
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.history import FileHistory
from prompt_toolkit.shortcuts import CompleteStyle, set_title
from prompt_toolkit.styles import Style

import steampipe_alchemy
from pacu import settings, utils


class Pacu:
    def __init__(self):
        self.steam = steampipe_alchemy.SteamPipe()
        self.modules = self.get_modules()

    @staticmethod
    def get_modules() -> Dict[str, ModuleType]:
        modules = {}
        for path in Path(settings.ROOT_DIR).glob(
            os.path.join('modules', '*', 'main.py')
        ):
            rel = path.relative_to(settings.ROOT_DIR)
            name = rel.parts[-2]
            mod_name = '.'.join(rel.parts)
            modules[name] = importlib.import_module(
                f"pacu.{mod_name.removesuffix('.py')}"
            )
        return modules

    @staticmethod
    def load_modules(app: 'typer.Typer'):
        """Check if app object exists and fallback to looking for the main function.

        The app method allows more customizations as well as multiple commands while the
         second, importing the main function is very simple. Below is an example of the
         later. See the typer docs for more details.

             import typer

             def main(name: str = 'test'):
                 typer.echo(f"Hello {name}")
        """

        modules = Pacu.get_modules()
        for name, mod in modules.items():

            try:
                app.add_typer(mod.app, name=name)  # type: ignore[attr-defined]
            except AttributeError:
                app.command(name=name)(mod.main)  # type: ignore[attr-defined]

    def start(self):
        self.steam.install(['aws'])
        regions = utils.get_all_regions()
        self.steam.update_config(aws={"plugin": "aws", "regions": regions})
        self.steam.start()


class PacuRepl(Pacu):
    def __init__(self):
        super().__init__()

        set_title("Pacu")

        self.style = Style.from_dict(
            {
                'completion-menu.completion': 'bg:#008888 #ffffff',
                'completion-menu.completion.current': 'bg:#00aaaa #000000',
                'scrollbar.background': 'bg:#88aaaa',
                'scrollbar.button': 'bg:#222222',
            }
        )
        self.history = FileHistory(os.path.expanduser("~/.pacu_history"))
        self.session: 'PromptSession' = PromptSession(
            history=self.history,
            auto_suggest=AutoSuggestFromHistory(),
            enable_history_search=True,
            completer=WordCompleter(list(self.get_modules().keys()), ignore_case=True),
            complete_style=CompleteStyle.READLINE_LIKE,
            style=self.style,
        )

    def repl(self):
        repl: 'typer.Typer' = typer.Typer()
        self.load_modules(repl)

        while True:
            try:
                t = self.session.prompt('> ')
                cmd = typer.main.get_command(repl)
                try:
                    cmd.main(shlex.split(t), standalone_mode=False)
                except Exception as e:  # pylint: disable=broad-except
                    print(e)

            except KeyboardInterrupt:
                pass
