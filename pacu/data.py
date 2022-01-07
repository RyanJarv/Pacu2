import json
from collections import Mapping
from typing import Optional

from tinydb import TinyDB
from tinydb.queries import QueryLike
from tinydb.storages import JSONStorage
from tinydb.table import Table, Document

from pacu.pacu import app_dir


def resource_name(id: str) -> str:
    if id.startswith('arn:aws:cloudformation:'):
        name = id.split(':')[5]
        if name.startswith('type/'):
            yield id.split('/')[3]
        else:
            yield id
    else:
        yield id


class CloudControlResource(Document):
    def __init__(self, value: Mapping, identifier: str, doc_id: int = None):
        super().__init__({
            "identifier": identifier,
            "properties": value,
        }, doc_id=doc_id)

    def to_json(self, *args, **kwargs) -> str:
        return json.dumps(self, *args, **kwargs)


class ResourceTable(Table):
    document_class = CloudControlResource
    document_id_class = str

    def __init__(self, name="default", *args, **kwargs):
        super().__init__(JSONStorage(app_dir/'resources.json'), name=name, *args, **kwargs)

    def get(self, cond: Optional[QueryLike] = None, doc_id: Optional[str] = None) -> Optional[CloudControlResource]:
        return super().get(cond, doc_id)


class ResourceDB(TinyDB):
    document_class = CloudControlResource
    document_id_class = str

    def __init__(self):
        super().__init__(f"{app_dir / self.__class__.__name__.lower()}.json")

    def get(self, cond: Optional[QueryLike] = None, doc_id: Optional[str] = None) -> Optional[CloudControlResource]:
        return super().get(cond, doc_id)

    def table(self, name: str, **kwargs) -> Table:
        return ResourceTable(name=name, **kwargs)

