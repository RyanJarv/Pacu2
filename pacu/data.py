import json
from collections import Mapping
from typing import Optional

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


class Resource(Document):
    def __init__(self, value: Mapping, doc_id: str):
        super().__init__(value, doc_id)

    def to_json(self, *args, **kwargs) -> str:
        return json.dumps(self, *args, **kwargs)


class ResourceDB(Table):
    document_class = Resource
    document_id_class = str

    def __init__(self):
        super().__init__(JSONStorage(f"{app_dir / self.__class__.__name__.lower()}.json"), "default")

    def get(self, cond: Optional[QueryLike] = None, doc_id: Optional[str] = None) -> Optional[Resource]:
        return super().get(cond, doc_id)

