from pathlib import Path
from typing import List, AnyStr

from tinydb import TinyDB, Query
from typing_extensions import get_type_hints
from typeguard import typechecked, check_type

from pacu.settings import app_dir

DEFAULTS = {
    'name': 'default',
    'regions': [
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-central-1",
            "eu-west-3",
            "eu-west-2",
            "eu-south-1",
            "eu-west-1",
            "eu-north-1",
            "af-south-1",
            "ap-south-1",
            "ap-northeast-3",
            "ap-northeast-2",
            "ca-central-1",
            "ap-northeast-1",
            "sa-east-1",
            "ap-east-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-southeast-3",
            "me-south-1",
        ]
}


def init_db(db_file: str, name: str) -> 'TinyDB':
    db = TinyDB(db_file)

    results = db.search(Query().name == name)
    if len(results) == 0:
        db.insert(DEFAULTS)
    return db


def set_profile(name):
    (Path(app_dir) / 'current_profile').write_text(name)


def get_profile():
    profile_path = (Path(app_dir) / 'current_profile')
    if profile_path.is_file():
        return profile_path.read_text()
    else:
        return 'default'


@typechecked
class Config(object):
    # Call's to __setattr__ are validated against the types listed here.
    regions: List[str]

    def __init__(self, name=False):
        if not name:
            name = get_profile()
        db = init_db(app_dir/'config.json', name)

        # This prevents recursive lookups.
        super().__setattr__('db', db)
        super().__setattr__('name', name)

        self.db: TinyDB = db
        self.name = name

    def __setattr__(self, key: AnyStr, value):
        if key in self.__dict__.keys():
            return super().__setattr__(key, value)

        # Validate the type passed is correct, the types at the top of this class is what is referenced here.
        try:
            check_type('regions', value, get_type_hints(self)[key])
        except KeyError:
            raise AttributeError(f"The '{self.name}' config profile has no key named '{key}'")

        self.db.upsert({"name": self.name, key: value}, Query().name == self.name)

    def __getattr__(self, key: AnyStr):
        resp = self.db.get(Query().name == self.name)
        if resp is None:
            raise AttributeError(f"No configuration named '{self.name}' was found.")
        else:
            try:
                return resp[key]
            except KeyError:
                raise AttributeError(f"The '{self.name}' config profile has no key named '{key}'")

    get = __getattr__
    set = __setattr__
