"""
Provides a dataclass template that is capable of loading from various config
file formats.
"""


import configparser
import json
import os
from dataclasses import dataclass

# set some bombs to explode later, for now
yaml = None  # pylint: disable=invalid-name
toml = None  # pylint: disable=invalid-name

try:
    import pyyaml
except ImportError:
    pass
try:
    import tomlkit  # use tomlkit.parse
except ImportError:
    pass


@dataclass
class PyConfigFile:
    """
    PyConfigFile: subclass this and add your dataclass attributes, eg:

    from configload import PyConfigFile

    class MyConfigClass(PyConfigFile):
        foo: int = 1
        yolo: bool = True

    # then initialize:
    myconfig = MyConfigClass(configfile="settings.ini")
    """

    configfiletypes = ("ini", "json")
    if yaml:
        configfiletypes = configfiletypes + ("yaml",)
    if tomlkit:
        configfiletypes = configfiletypes + ("toml",)

    def __init__(self, configfile=None, configfiletype=None, *args, **kwargs):

        # first initialize data class
        super(PyConfigFile).__init__(*args, **kwargs)

        # now, optionally run the config file loader
        self.configfile = configfile

        if self.configfile:
            self.configfiletype = configfiletype or self.configfile_to_filetype(
                self.configfile
            )
            if self.configfiletype not in self.configfiletypes:
                raise UserWarning(f"Unsupported file type {self.configfiletypes}")
            raise NotImplementedError()

    @staticmethod
    def configfile_to_filetype(configfile):
        """Naive extension check to set configfiletype from path"""
        ext = None
        try:
            ext = os.path.splitext(configfile)[1]
        except IndexError:
            pass

        if ext and ext in self.configfiletypes:
            return ext

        raise UserWarning(f"Can't figure out file type for {configfile}")

    @staticmethod
    def ini_loader(configfile):
        raise NotImplementedError("yaml not enabled")

    @staticmethod
    def json_loader(configfile):
        raise NotImplementedError("yaml not enabled")

    @staticmethod
    def toml_loader(configfile):
        raise NotImplementedError("yaml not enabled")

    @staticmethod
    def yaml_loader(configfile):
        """Load a yaml file, return a python dictionary"""
        if not yaml:
            raise NotImplementedError("yaml not enabled")
        with open(configfile, "r") as infile:
            return yaml.load(infile, Loader=yaml.FullLoader)

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
