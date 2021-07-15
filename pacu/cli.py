import typer

from pacu.pacu import PacuRepl


app = typer.Typer()

pacu = PacuRepl()
pacu.load_modules(app)


@app.command('repl')
def repl():
    pacu.start()
    pacu.repl()


if __name__ == '__main__':
    app(prog_name="pacu")
