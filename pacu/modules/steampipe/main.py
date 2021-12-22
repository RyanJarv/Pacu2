# import subprocess
#
# import steampipe_alchemy
# from pacu import utils
# import typer
#
# app = typer.Typer()
#
# steam = steampipe_alchemy.SteamPipe()
#
#
# @app.command()
# def install():
#     steam.install(['aws'])
#     regions = utils.get_all_regions()
#     steam.update_config(aws={"plugin": "aws", "regions": regions})
#
#
# @app.command()
# def start():
#     steam.start(shutdown_on_exit=False)
#
#
# @app.command()
# def stop():
#     steam.stop()
#
#
# @app.command()
# def query():
#     steam.cli('query')
#
#
# @app.command()
# def restart():
#     steam.stop()
#
#
# if __name__ == "__main__":
#     app()
