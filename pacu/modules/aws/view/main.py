import asyncio

import sqlite3
import sys

import steampipe_alchemy
import sqlite_utils
import sqlite_utils.cli
import typer
from sqlalchemy import inspect, inspection
from steampipe_alchemy import models

from . import cli

app = typer.Typer()

class Scan:
    def __init__(self):
        self.sem = asyncio.BoundedSemaphore(60)
        self.steam = steampipe_alchemy.SteamPipe()
        self.steam.status()
        self.skip = [
            'AwsEc2SslPolicy',

            # Shared/Public
            'AwsSsmDocument',
            'AwsEc2AmiShared',
            'AwsVpcEndpointService',

            # No need to retrieve on demand
            'AwsEc2InstanceType',
            'AwsIamAction',

            # Needs conditional
            'AwsIamPolicySimulator',
            'AwsAppautoscalingTarget',
            'AwsSsmManagedInstanceCompliance',

            # Needs initial setup
            'AwsAuditmanagerEvidence',
            'AwsAuditmanagerEvidenceFolder',
            'AwsAuditmanagerFramework',
            'AwsAuditmanagerControl',
            'AwsAuditmanagerAssessment',
        ]

    async def run(self):
        # self.db.table
        # self.db.table("AwsIamRole", columns={"arn": str, "id": str})
        # self.db.table("AwsAccount", columns={"account_id": str})
        # # self.db.create_table("AwsVpc")
        # # self.db.create_table("AwsVpcRouteTable")
        # # self.db.create_table("AwsVpcInternetGateway")
        # # self.db.create_table("AwsVpcEgressOnlyInternetGateway")
        # # self.db.create_table("AwsLambdaFunction")
        # # self.db.create_table("AwsVpcEgressOnlyInternetGateway")
        # # self.db.create_table("AwsEc2NetworkInterface")
        # # self.db.create_table("AwsVpcRouteTable")
        # self.db.table("AwsCloudwatchLogGroup", columns={"name": str})
        # self.db.table("AwsSnsTopic", columns={"topic_arn": str})
        # # self.db.create_table("AwsS3Bucket")

        db_fk = {}

        for svc in filter(lambda s: s.startswith('Aws'), dir(models)):
            if svc in self.skip:
                continue
            await self.sem.acquire()
            print("adding " + str(svc))
            task = asyncio.to_thread(self.query, db_fk, svc)
            await asyncio.sleep(0.01)
            await task

        print("waiting on queries")
        # await asyncio.gather(*tasks)

        # self.db.add_foreign_keys([
        #     ("AwsIamAccessKey", "user_name", "AwsIamUser", "title"),
        #     ("AwsIamVirtualMfaDevice", "user_name", "AwsIamUser", "title"),
        #     ("AwsIamRole", "account_id", "AwsAccount", "account_id"),
        #     ("AwsAccount", "organization_master_account_id", "AwsAccount", "account_id"),
        # ])

        db = sqlite_utils.Database('./dump.db')
        for svc, fks in db_fk.items():
            for fk in fks:
                try:
                    print(f"updating foreign keys on {svc}")
                    db[svc].add_foreign_key(*fk, ignore=True)
                except Exception as e:
                    print(e)
                    import pdb;
                    pdb.set_trace()
                    continue

    def query(self, db_fk, svc):
        db = sqlite_utils.Database('./dump.db')
        print(f"Service: {str(svc)}")
        try:
            print("svc: " + str(svc))
            model = getattr(models, svc)
            model_info = inspect(model)
            pk = model_info.primary_key[0]
            for i, row in enumerate(self.steam.query(model).all()):
                print('.', file=sys.stderr)

                print(f"pk: {pk.name} {getattr(row, pk.name)}")
                table_fk = []

                if 'user_id' in model_info.columns.keys():
                    table_fk.append(("user_id", "AwsIamUser", "user_id"))

                if 'region' in model_info.columns.keys():
                    table_fk.append(("region_name", "AwsRegion", "region"))

                if 'region_name' in model_info.columns.keys():
                    table_fk.append(("region_name", "AwsRegion", "region"))

                if 'account_id' in model_info.columns.keys():
                    table_fk.append(("account_id", "AwsAccount", "account_id"))
                if 'aws_account_id' in model_info.columns.keys():
                    table_fk.append(("aws_account_id", "AwsAccount", "account_id"))
                if 'owner' in model_info.columns.keys():
                    table_fk.append(("owner", "AwsAccount", "account_id"))
                if 'owner_id' in model_info.columns.keys():
                    table_fk.append(("owner_id", "AwsAccount", "account_id"))
                if 'association_ip_owner_id' in model_info.columns.keys():
                    table_fk.append(("association_ip_owner_id", "AwsAccount", "account_id"))
                if 'registry_id' in model_info.columns.keys():
                    table_fk.append(("registry_id", "AwsAccount", "account_id"))
                if 'created_by' in model_info.columns.keys():
                    table_fk.append(("created_by", "AwsAccount", "account_id"))
                if 'instance_owner_id' in model_info.columns.keys():
                    table_fk.append(("instance_owner_id", "AwsAccount", "account_id"))
                if 'attached_instance_owner_id' in model_info.columns.keys():
                    table_fk.append(("attached_instance_owner_id", "AwsAccount", "account_id"))

                # these tables seem to be missing
                # if 'attached_instance_id' in model_info.columns.keys():
                #     table_fk.append(("owner", "AwsAccount", "account_id"))
                #
                # if 'snapshot_id' in model_info.columns.keys():
                #     table_fk.append(("snapshot_id", "...", "..."))

                if 'vpc_id' in model_info.columns.keys():
                    table_fk.append(("vpc_id", "AwsVpc", "vpc_id"))

                if 'network_acl_id' in model_info.columns.keys():
                    table_fk.append(("network_acl_id", "AwsVpcNetworkAcl", "network_acl_id"))

                if 'user_name' in model_info.columns.keys():
                    table_fk.append(("user_name", "AwsIamUser", "name"))

                if 'availability_zone' in model_info.columns.keys():
                    table_fk.append(("availability_zone", "AwsAvailabilityZone", "name"))

                if 'availability_zone_id' in model_info.columns.keys():
                    table_fk.append(("availability_zone_id", "AwsAvailabilityZone", "zone_id"))

                if 'parent_zone_id' in model_info.columns.keys():
                    table_fk.append(("parent_zone_id", "AwsAvailabilityZone", "zone_id"))

                if 'network_interface_id' in model_info.columns.keys():
                    table_fk.append(("network_interface_id", "AwsEc2NetworkInterface", "network_interface_id"))

                if 'route_table_id' in model_info.columns.keys():
                    table_fk.append(("route_table_id", "AwsVpcRouteTable", "route_table_id"))

                if 'gateway_id' in model_info.columns.keys():
                    table_fk.append(("gateway_id", "AwsVpcInternetGateway", "internet_gateway_id"))

                # id is wrong?
                # if 'egress_only_internet_gateway_id' in model_info.columns.keys():
                #     table_fk.append(("egress_only_internet_gateway_id", "AwsVpcEgressOnlyInternetGateway", "id"))

                if 'function_name' in model_info.columns.keys():
                    table_fk.append(("function_name", "AwsLambdaFunction", "name"))

                if 'role' in model_info.columns.keys():
                    table_fk.append(("role", "AwsIamRole", "arn"))
                if 'iam_role_arn' in model_info.columns.keys():
                    table_fk.append(("iam_role_arn", "AwsIamRole", "arn"))
                if 'cloudwatch_logs_role_arn' in model_info.columns.keys():
                    table_fk.append(("cloudwatch_logs_role_arn", "AwsIamRole", "arn"))
                if 'service_role' in model_info.columns.keys():
                    table_fk.append(("service_role", "AwsIamRole", "arn"))
                if 'role_arn' in model_info.columns.keys():
                    table_fk.append(("role_arn", "AwsIamRole", "arn"))
                if 'execution_role_arn' in model_info.columns.keys():
                    table_fk.append(("execution_role_arn", "AwsIamRole", "arn"))
                if 'task_role_arn' in model_info.columns.keys():
                    table_fk.append(("task_role_arn", "AwsIamRole", "arn"))
                if 'deliver_logs_permission_arn' in model_info.columns.keys():
                    table_fk.append(("deliver_logs_permission_arn", "AwsIamRole", "arn"))

                if 'file_system_id' in model_info.columns.keys():
                    table_fk.append(("file_system_id", "AwsEfsFileSystem", "file_system_id"))

                if 'rotation_lambda_arn' in model_info.columns.keys():
                    table_fk.append(("rotation_lambda_arn", "AwsLambdaFunction", "arn"))

                if 'dhcp_options_id' in model_info.columns.keys():
                    table_fk.append(("dhcp_options_id", "AwsVpcDhcpOptions", "dhcp_options_id"))

                if 'group_id' in model_info.columns.keys():
                    table_fk.append(("group_id", "AwsVpcSecurityGroup", "group_id"))

                if 'log_group_arn' in model_info.columns.keys():
                    table_fk.append(("log_group_arn", "AwsCloudwatchLogGroup", "arn"))
                if 'log_group_name' in model_info.columns.keys():
                    table_fk.append(("log_group_name", "AwsCloudwatchLogGroup", "name"))
                if 'log_destination' in model_info.columns.keys():
                    table_fk.append(("log_destination", "AwsCloudwatchLogGroup", "arn"))

                if 'topic_arn' in model_info.columns.keys():
                    table_fk.append(("topic_arn", "AwsSnsTopic", "topic_arn"))
                if 'endpoint' in model_info.columns.keys():
                    table_fk.append(("endpoint", "AwsLambdaFunction", "arn"))
                if 'sns_topic_arn' in model_info.columns.keys():
                    table_fk.append(("sns_topic_arn", "AwsSnsTopic", "topic_arn"))
                if 'kms_key_id' in model_info.columns.keys():
                    table_fk.append(("kms_key_id", "AwsKmsKey", "id"))
                if 's3_bucket_name' in model_info.columns.keys():
                    table_fk.append(("s3_bucket_name", "AwsS3Bucket", "name"))

                db_fk[svc] = table_fk

                # try:
                #     db[svc].upsert(row.to_dict(), pk=pk.name, alter=True)
                # except sqlite3.IntegrityError:
                #     db[svc].transform(pk=pk.name, drop=True)
                #     db[svc].upsert(row.to_dict(), pk=pk.name, alter=True)
        except Exception as e:
            print(f"Caught exception: {e}")
            self.steam.db.rollback()
        finally:
            self.sem.release()
            print("done: " + str(svc))

@app.command()
def view():
    cli.run()

@app.command()
def scan():
    asyncio.run(Scan().run())


