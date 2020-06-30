"""
Provides a dataclass template that is capable of loading from various config
file formats.
"""


import configparser
import json
import os
from dataclasses import dataclass

try:
    import pyyaml
    import tomlkit  # use tomlkit.parse
except ImportError:
    # set some bombs to explode later, for now
    pyyaml = None
    toml = None


@dataclass
class PyConfigFile:
    """
    PyConfigFile: subclass this and add your dataclass attributes, eg:

    from py_configfile import PyConfigFile

    class MyConfigClass(PyConfigFile):
        foo: int = 1
        yolo: bool = True

    # then initialize:
    myconfig = MyConfigClass(configfile="settings.ini")
    """

    configfiletypes = ("ini", "json")
    if pyyaml:
        configfiletypes = configfiletypes + ("yaml",)

    def __init__(self, configfile=None, configfiletype=None, *args, **kwargs):

        # first initialize data class
        super(PyConfigFile).__init__(*args, **kwargs)

        # now, optionally run the config file loader
        self.configfile = configfile

        if self.configfile:
            self.configfiletype = configfiletype or self.configfile_to_filetype(
                self.configfile
            )
            raise NotImplementedError()

    @staticmethod
    def configfile_to_filetype(configfile):
        """Naive extension check to set configfiletype from path"""
        raise NotImplementedError()

    def config_file_loader(self):
        # for ini, catch and raise configparser.MissingSectionHeaderError

        raise NotImplementedError()

    def load_environment(self, prefix=""):
        """
        Load environment variables into the config.

        They'll be of the form <prefix_><dataclass attribute>.upper(), eg:

        class MyConfigClass(PyConfigFile):
            user_setting: str = "heyo"

        myconfig = MyConfigClass()

        # this will load "USER_SETTING" variable from the environment, and
        # convert it to the type of the dataclass attribute
        myconfig.load_environment()
        """
        raise NotImplementedError()
