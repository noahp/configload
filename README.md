[![Code style:
black](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge)](https://github.com/ambv/black)
[![GitHub Workflow
Status](https://img.shields.io/github/workflow/status/noahp/py-configfile/main-ci?style=for-the-badge)](https://github.com/noahp/py-configfile/actions)
[![PyPI
version](https://img.shields.io/pypi/v/py-configfile.svg?style=for-the-badge)](https://pypi.org/project/py-configfile/)
[![PyPI
pyversions](https://img.shields.io/pypi/pyversions/py-configfile.svg?style=for-the-badge)](https://pypi.python.org/pypi/py-configfile/)
[![License:
MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

- [Install](#install)
- [Usage](#usage)
- [Limitations](#limitations)
  - [`.ini` specific](#ini-specific)
- [Config File Formats](#config-file-formats)

<!-- omit in toc -->
# py-configfile

Teeny package to support loading a dataclass from a config file (`.ini`,
`.json`, optionall with extensions `.yaml`, `.toml`).

## Install

```bash
# install with extras: support for yaml and toml (requires extra dependencies)
pip install py-configfile[yaml,toml]
```

## Usage

Instantiate a child class like so:

```python
from py_configfile import PyConfigFile

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

### `.ini` specific

The `.ini` format has section markers (eg `[DEFAULT]`) as optional, but the
python standard library configparser requires at least one section marker.

This library (`py-configfile`) will _only_ parse keys from the `[DEFAULT]`
section, all other sections are ignored.

If the ini file doesn't contain a `[DEFAULT]` section an error will be raised.

## Config File Formats

Subjective comparision:

- `.ini` - built into python standard library, supports comments, no types
- `.json` - built in, no comments 😞, types
- `.yaml` - not built in, comments, types
- `.toml` - not built in, comments, types
