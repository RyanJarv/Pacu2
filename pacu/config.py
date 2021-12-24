import os
from pathlib import Path
from typing import List, AnyStr

import typer
from tinydb import TinyDB, Query
from typing_extensions import get_type_hints
from typeguard import typechecked, check_type

from pacu.settings import app_dir

DEFAULTS = {
    'namespace': 'default',
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


def init_db(db_file: str, namespace: str) -> 'TinyDB':
    db = TinyDB(db_file)

    results = db.search(Query().namespace == namespace)
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
class PersistentClass(object):
    """PersistentClass is a class that persists instance properties of it's subclasses to a JSON file on disk.

        To make use of it you can subclass PersistentClass and add type hints for all valid properties of that class. The
    type hints are enforced at runtime so you are guaranteed the properties will be the specified type. When the class
    is created you can either pass the file path to where the backing JSON file should be saved or by default it will
    create a file named after the class name in Pacu's config directory. You also have the option of setting a profile
    on instantiation, this act's as a namespace allowing you to have multiple configurations using the same backing
    file. The

    > conf = SubclassOfPersistentClass(namespace='ryan_jarv')

        With the instance created you can set and use properties on the class as needed and they will be kept in sync
    with the JSON file backing the object. The set and get methods also exist as an alternative to managing the object
    with properties.

    > conf.twitter = '@ryan_jarv'
    > conf.twitter
    @ryan_jarv
    """

    def cmd(self, args: List[str]):
        """cmd provides similar functionality to properties but exposed through command line arguments.

        Behavior will differ based on the arguments passed as follows:
            No Arguments: Return string of the JSON backing this class.
            One Argument: Used to look up a key name and return the value associated with it.
            Two or more arguments: Use first as a key name whose value is set to the value of the remaining arguments.
        """
        if len(args) == 0:
            return self.db.all()
        elif len(args) == 1:
            return self.get(args[0])
        elif len(args) == 2:
            # Try setting the value as a string first, if that fails try a list
            try:
                self.set(args[0], args[1])
            except TypeError:
                self.set(args[0], [args[1]])
        else:
            self.set(args[0], args[1:])
        return self.get(args[0])

    def __init__(self, path: str = None, namespace: str = 'default'):
        if path:
            db = init_db(path, namespace)
        else:
            db = init_db(f"{app_dir/self.__class__.__name__.lower()}.json", namespace)

        # This prevents recursive lookups.
        super().__setattr__('db', db)
        super().__setattr__('namespace', namespace)

        self.db: TinyDB = db
        self.namespace = namespace

    def __setattr__(self, key: AnyStr, value):
        if key in self.__dict__.keys():
            return super().__setattr__(key, value)

        # Validate the type passed is correct, the types at the top of this class is what is referenced here.
        try:
            check_type('regions', value, get_type_hints(self)[key])
        except KeyError:
            raise AttributeError(f"The '{self.namespace}' {self.__class__.__name__} profile has no key named '{key}'")

        self.db.upsert({"namespace": self.namespace, key: value}, Query().namespace == self.namespace)

    def __getattr__(self, key: AnyStr):
        resp = self.db.get(Query().namespace == self.namespace)
        if resp is None:
            raise AttributeError(f"No {self.__class__.__name__} key named '{self.namespace}' was found.")
        else:
            try:
                return resp[key]
            except KeyError:
                raise AttributeError(f"The '{self.namespace}' {self.__class__.__name__} has no key named '{key}'")

    get = __getattr__
    set = __setattr__


class Config(PersistentClass):
    def __init__(self, profile=None):
        if not profile:
            profile = get_profile()
        super().__init__(namespace=profile)

    regions: List[str]


class Credentials(PersistentClass):
    def __init__(self, config: str, profile: str = None):
        p = app_dir/config/'credentials.json'
        os.mkdir(p.parent)
        super().__init__(path=p, namespace=profile)

    regions: List[str]
