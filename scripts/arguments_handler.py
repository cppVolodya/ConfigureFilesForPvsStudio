import os

import scripts.text_manipulator as TextManipulator

from scripts.main_data import *


class ArgumentsHandler:
    def __init__(self, arguments):
        self.m_arguments = arguments
        self.m_text_manipulator = TextManipulator.TextManipulator(self.m_arguments.extensions)

    def Start(self):
        self.HandleAddCommand()
        self.HandleRemoveCommand()

    def HandleAddCommand(self):
        if self.m_arguments.add:
            for directory in self.m_arguments.add:
                if not os.path.exists(directory):
                    print(DEFAULT_DIRECTORY_ERROR_MESSAGE + directory)
                else:
                    self.m_text_manipulator.AddTextToFilesInDirectory(directory)

    def HandleRemoveCommand(self):
        if self.m_arguments.remove:
            for directory in self.m_arguments.remove:
                if not os.path.exists(directory):
                    print(DEFAULT_DIRECTORY_ERROR_MESSAGE + directory)
                else:
                    self.m_text_manipulator.RemoveTextFromFilesInDirectory(directory)
