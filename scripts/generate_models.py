#!/usr/bin/env python3

import json
import botocore.loaders
import black
import boto3
import botocore.session
import botocore.config
import typer

from pathlib import Path
from typing import List, TYPE_CHECKING, Generator, Dict, OrderedDict
from datamodel_code_generator import InputFileType, generate, PythonVersion, model
from datamodel_code_generator.model.pydantic import DataTypeManager
from datamodel_code_generator.model.pydantic.base_model import BaseModel, DataModelField, Constraints
from datamodel_code_generator.reference import Reference
from datamodel_code_generator.types import DataType, Types

if TYPE_CHECKING:
    import mypy_boto3_cloudformation
    from mypy_boto3_cloudformation import type_defs as cfn_t

app = typer.Typer()

schema_dir = Path(__file__).parents[1] / 'pacu/data/schema'
models_dir = Path(__file__).parents[1] / 'pacu/models'


def get_schemas(sess: 'boto3.Session', config: 'botocore.config.Config' = None) -> Generator['cfn_t.DescribeTypeOutputTypeDef', None, None]:
    cfn: 'mypy_boto3_cloudformation.Client' = sess.client('cloudformation')

    paginator = cfn.get_paginator('list_types')
    types: List['cfn_t.TypeSummaryTypeDef'] = []

    list_types_input = {
        "Visibility": 'PUBLIC',
        "Filters": {'Category': 'AWS_TYPES'},
        "Type": 'RESOURCE',
        "DeprecatedStatus": 'LIVE',
    }
    for page in paginator.paginate(**list_types_input):
        types.extend(page['TypeSummaries'])
        for t in page['TypeSummaries']:
            yield cfn.describe_type(Type='RESOURCE', TypeName=t['TypeName'])


@app.command()
def schema():
    config = botocore.config.Config(
        retries={
            'max_attempts': 6,
            'mode': 'adaptive'
        }
    )
    sess = boto3.Session()
    for s in get_schemas(sess, config):
        print(s['TypeName'])
        path = schema_dir/f"{s['TypeName']}.json"

        s = json.loads(s['Schema'])
        s = json.dumps(s, indent=True)
        path.write_text(s)


def required(shape: OrderedDict[str, OrderedDict]) -> bool:
    if shape.get('required'):
        return True
    else:
        return False


def constraints(shape: OrderedDict[str, OrderedDict]) -> Constraints:
    kwargs = {}
    if shape.get('pattern'):
        kwargs['regex'] = shape['pattern']

    for k in shape.keys():
        if k not in ['type', 'pattern']:
            import pdb; pdb.set_trace()

    return Constraints(**kwargs)


def structure(sname: str, shape: OrderedDict) -> BaseModel:
    fields: List[DataModelField] = []
    for mname, _type in shape['members'].items():
        fields.append(DataModelField(
            name=mname,
            data_type=DataType(type=_type['shape']),
            required=required(shape),
        ))
    return BaseModel(
        reference=Reference(name=sname, path='.'),
        fields=fields,
    )


@app.command()
def models():
    # data_manager = DataTypeManager(
    #     python_version=PythonVersion.PY_38,
    #     use_standard_collections=False,
    #     use_generic_container_types=False,
    #     strict_types=[],
    # )
    # return
    loader = botocore.loaders.create_loader()
    for svc in loader.list_available_services('service-2'):
        listable = []
        latest = loader.determine_latest_version(svc, 'service-2')
        model: OrderedDict[str, OrderedDict] = loader.load_service_model(svc, 'service-2', latest)
        shapes: OrderedDict[str, OrderedDict] = dict(model['shapes'])

        objs = {}
        for sname, shape in shapes.items():
            objs[sname] = obj_from_shape(shape, sname)

        break

        # # print(shapes['PrincipalArn'])
        # for name, op in model['operations'].items():
        #     shape = dict(shapes[op['input']['shape']])
        #     if not shape.get('required'):
        #         listable.append(name)
        #
        #     print(shape.keys())
        #     for member in op['members']:
        #         print(shapes.keys())
        #         print(shapes[member])
        #         break
        #     break
        # break
        #
    # m = BaseModel(
    #     reference=Reference(path='.', name='test'),
    #     fields=[DataModelField(name='test', data_type=DataType(type='str'), required=True)],
    # )
    # print(m.render())
    #

    # for s in schema_dir.glob('*'):
    #     name = ''.join(s.name.split('.')[:-1])
    #     filename = [p.capitalize() for p in str(name).split('::')]
    #     filename = ''.join(filename)
    #
    #     path = models_dir/f"{filename}.py"
    #     try:
    #         generate(
    #             s,
    #             input_file_type=InputFileType.JsonSchema,
    #             input_filename="example.json",
    #             use_schema_description=True,
    #             reuse_model=True,
    #             target_python_version=PythonVersion.PY_38,
    #             output=path,
    #         )
    #     except Exception as e:
    #         print(f"Failed to generate model for '{s.name}': {e}")
    #         continue


def obj_from_shape(shape, sname):
    if shape['type'] == 'structure':
        return structure(sname, shape)
    elif shape['type'] == 'string':
        return DataModelField(
            name=sname,
            data_type=DataType(type='String'),
            required=required(shape),
            constraints=constraints(shape)
        )
    elif shape['type'] == 'list':
        d = DataModelField(
            name=sname,
            data_type=DataType(type='List', is_list=True, is_custom_type=True),
            required=required(shape),
            constraints=shape,
        )
        print(d)
        return d
    else:
        import pdb;
        pdb.set_trace()


if __name__ == '__main__':
    app()