"""
Provides a dataclass template that is capable of loading from various config
file formats.
"""


import json
import os

import config
import dataclass

try:
    import pyyaml
    import tomlkit  # use tomlkit.parse
except ImportError:
    # set some bombs to explode later, for now
    pyyaml = None
    toml = None


@dataclass.dataclass
class PyConfigFile:
    """
    PyConfigFile: subclass this and add your dataclass attributes, eg:

    from py_configfile import PyConfigFile

    class MyConfigClass(py_configfile.PyConfigFile):
        foo: int = 1
        yolo: bool = True

    # then initialize:
    myconfig = MyConfigClass(configfile="settings.ini")
    """

    def __init__(self, configfile=None, configfiletype=None, *args, **kwargs):

        # first initialize data class
        super(PyConfigFile).__init__(*args, **kwargs)

        # now, optionally run the config file loader
        self.configfile = configfile
        self.configfiletype = configfiletype

        if self.configfile:
            pass

    @staticmethod
    def configfile_to_filetype(configfile):
        """Naive extension check to set configfiletype from path"""

        pass

    def config_file_loader(self):
        pass
