# import typing
#
# import boto3
# import typer
#
# import pacu.data as p
#
#
# if typing.TYPE_CHECKING:
#     from mypy_boto3_iam import type_defs as t
#     from mypy_boto3_iam.client import IAMClient
#     from mypy_boto3_iam.paginator import ListRolesPaginator
#
#
# def fetch(profile_name: typing.Optional[str] = typer.Option(default=None)):
#     sess = boto3.session.Session(profile_name=profile_name)
#     iam: IAMClient = sess.client('iam')
#     paginator: ListRolesPaginator = iam.get_paginator('list_roles')
#     page_iterator: typing.Iterator[t.ListRolesResponseTypeDef] = paginator.paginate()
#     for page in page_iterator:
#         p.db["roles"].insert_all(page['Roles'], pk="RoleName")
#
#
# if __name__ == '__main__':
#     typer.run(fetch)
