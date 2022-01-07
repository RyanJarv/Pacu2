import json
import typer

from .browse import browse

from pathlib import Path
from datamodel_code_generator import InputFileType, generate

from pacu.aws import get_schemas, default_region
from pacu.data import ResourceDB, ResourceTable


app = typer.Typer(help='Data management commands')
app.command()(browse)


@app.command()
def types():
    for table in ResourceDB().tables():
        print(table)


@app.command()
def list(type: str = typer.Argument(False)):
    db = ResourceDB()
    tables = []
    if type:
        if type not in db.tables():
            print(f"The type {type} is not valid.")
            return

        for i in ResourceTable(type).all():
            print(i)

        tables.append(db.table(type))
    else:
        for table in db.tables():
            tables.append(db.table(table))

    for table in tables:
        # import pdb; pdb.set_trace()
        for r in table.all():
            print('asf')
            print(r)


@app.command()
def update_models():
    _update_models()


@default_region()
def _update_models(sess, region):
    for schema in get_schemas(sess):
        filename = ''.join([p.capitalize() for p in str(schema['typeName']).split('::')])

        path = Path(__file__).parents[2]/'models'/f"{filename}.py"
        generate(
            json.dumps(schema),
            input_file_type=InputFileType.JsonSchema,
            input_filename="example.json",
            output=path,
        )

if __name__ == '__main__':
    app()



