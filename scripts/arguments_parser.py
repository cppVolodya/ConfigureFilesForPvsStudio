import argparse

from scripts.main_data import *


class ArgumentsParser:
    def __init__(self):
        self.m_parser    = None
        self.m_arguments = None

    def Start(self):
        self.Parse()
        self.Validate()

    def Parse(self):
        self.m_parser = argparse.ArgumentParser(description = DEFAULT_ADD_AND_REMOVE_MESSAGE)
        self.m_parser.add_argument("-add",        nargs = "+", help = DEFAULT_DIRECTORIES_TO_ADD_MESSAGE)
        self.m_parser.add_argument("-remove",     nargs = "+", help = DEFAULT_DIRECTORIES_TO_REMOVE_MESSAGE)
        self.m_parser.add_argument("-extensions", nargs = "*", help = DEFAULT_EXTENSIONS_MESSAGE, default = DEFAULT_FILE_EXTENSIONS)
        self.m_arguments = self.m_parser.parse_args()

    def Validate(self):
        if not self.m_arguments.add and not self.m_arguments.remove:
            print(DEFAULT_PARAMETER_ERROR_MESSAGE)
            return False
        return True

    def GetArgs(self):
        return self.m_arguments
