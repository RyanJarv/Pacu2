Note: This was mostly a scratch space for various ideas. Check out [pacu3](https://github.com/RyanJarv/pacu3) for the (initial) rewrite.

# Overview

The AWS exploitation framework, designed for testing the security of Amazon Web Services environments.

This project was generated with [cookiecutter](https://github.com/audreyr/cookiecutter) using [jacebrowning/template-python](https://github.com/jacebrowning/template-python).

[![Unix Build Status](https://img.shields.io/travis/com/RyanJarv/pacu.svg?label=unix)](https://travis-ci.com/RyanJarv/pacu)
[![Windows Build Status](https://img.shields.io/appveyor/ci/RyanJarv/pacu.svg?label=windows)](https://ci.appveyor.com/project/RyanJarv/pacu)
[![Coverage Status](https://img.shields.io/codecov/c/gh/RyanJarv/pacu)](https://codecov.io/gh/RyanJarv/pacu)
[![Scrutinizer Code Quality](https://img.shields.io/scrutinizer/g/RyanJarv/pacu.svg)](https://scrutinizer-ci.com/g/RyanJarv/pacu)
[![PyPI Version](https://img.shields.io/pypi/v/pacu.svg)](https://pypi.org/project/pacu)
[![PyPI License](https://img.shields.io/pypi/l/pacu.svg)](https://pypi.org/project/pacu)

# Usage

```bash
$ make docker/dev
$ python -m pacu repl
>
> ** tab **
items users
>
> users
Usage: __main__.py users [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  create
  delete
>
> users create my_user
Creating user: my_user
```

Or alternatively:
```
$ python3 -m pacu users create my_user
Creating user: my_user
```

Note: The `python3 -m pacu` part is only needed for dev, typically it would just be `pacu`.


# Features
* Full featured command prompt using much less code then pacu
  * (REPL Code)[https://github.com/RhinoSecurityLabs/pacu2/blob/3ad5877b0181b087e11a5cd32395c5653f1bae5d/pacu/pacu.py#L68]
  * Features: Reverse search, auto-complete w/ suggestions, history across sessions.
* Commands can be ran the same way in the REPL as executed directly
  * `pacu users` in the system shell is the same as `users`
* Simplified modules
* Access to steampipe via [steampipe_alchemy](https://github.com/RyanJarv/steampipe_alchemy).
  * Currently this is installed and started at runtime, but usage from inside a module is a WIP.


## Simplified modules
This is a valid module:

```
def main(name: str = 'test'):
  print(f"Hello {name}")
```

It can be run as `pacu module_name`, or in the repl as `module_name`. It takes an optional string argument `name`, which
defaults to `test` and outputs a help when run with `--help`.

```
> items --help
Usage: __main__.py items [OPTIONS]

Options:
  --name TEXT  [default: test]
  --help       Show this message and exit.
> items
Hello test
> items --name world
Hello world
```

