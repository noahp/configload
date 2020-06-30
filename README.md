[![GitHub](https://img.shields.io/badge/GitHub-noahp/configload-8da0cb?style=for-the-badge&logo=github)](https://github.com/noahp/configload)
[![Code style:
black](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge)](https://github.com/ambv/black)
[![GitHub Workflow
Status](https://img.shields.io/github/workflow/status/noahp/configload/main-ci?style=for-the-badge)](https://github.com/noahp/configload/actions)
[![PyPI
version](https://img.shields.io/pypi/v/configload.svg?style=for-the-badge)](https://pypi.org/project/configload/)
[![PyPI
pyversions](https://img.shields.io/pypi/pyversions/configload.svg?style=for-the-badge)](https://pypi.python.org/pypi/configload/)
[![License:
MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

- [Install](#install)
- [Usage](#usage)
- [Limitations](#limitations)
  - [Flat structure](#flat-structure)
  - [Simple types only](#simple-types-only)
  - [`.ini` default section](#ini-default-section)
- [Config File Formats](#config-file-formats)

<!-- omit in toc -->
# configload

**NOTE: not functional yet!!!**

Teeny package to support loading a dataclass from a config file (`.ini`,
`.json`; optionally, with extensions `.yaml`, `.toml`).

_Note: [dynaconf](https://github.com/rochacbruno/dynaconf) is a **much** more
featureful implementation of a similar idea, so for anything serious it might be
a better choice! see also [configloader](https://pypi.org/project/configloader/)
for another similar implementation_

## Install

```bash
# install with extras: support for yaml and toml (requires extra dependencies)
pip install configload[yaml,toml]
```

## Usage

Instantiate a child class like so:

```python
from configload import PyConfigFile

class MyConfigClass(PyConfigFile):
    # setting defaults makes it simpler to instantiate
    yolo: int = 1234
    heyo: str = "hi!"
    numbertime: float = 1.23

myconfig = MyConfigClass(configfile="settings.ini")

# keys from "settings.ini" that match fields in the dataclass will be converted
# to specified types and loaded into myconfig. unknown keys are silently skipped
```

## Limitations

### Flat structure

To keep things consistent between ini and structured formats, and due to the
limitations of dataclasses, really only top-level (flat) structure is suited to
this.

For example, this JSON:

```json
{
    "top_level_key": {
        "nested_key": 1
    }
}
```

Will result in a dataclass with a `dict` field `.top_level_key`, but after that,
nested values will have to use dict semantics, i.e.:

```python
# to access nested keys:
myconfig.top_level_key["nested_key"]
```

### Simple types only

Only simple dataclass types (`str`, `int`, `list`, `dict`, etc) are supported,
and ini format only supports scalar types.

_**TODO**_ support may be added for more complex data types by using
`ast.literal_eval` to convert string repr of a data structure in an ini key
value, but this is:

- kinda sketchy, error prone
- might not be that useful anyway 🤷

Example might be:

```ini
[DEFAULT]
# python string repr of a dictionary
key_1 = { "nested_key": 123, }
```

### `.ini` default section

The `.ini` format has section markers (eg `[DEFAULT]`) as optional, but the
python standard library configparser requires at least one section marker.

This library (`configload`) will _only_ parse keys from the `[DEFAULT]`
section, all other sections are ignored.

If the ini file doesn't contain a `[DEFAULT]` section an error will be raised.

## Config File Formats

Subjective comparision:

- `.ini` - built into python standard library, supports comments, no types
- `.json` - built in, no comments 😞, types
- `.yaml` - not built in, comments, types
- `.toml` - not built in, comments, types
