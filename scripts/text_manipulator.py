import os

from scripts.main_data import *


class TextManipulator:
    def __init__(self, extensions):
        self.m_text = DEFAULT_SPECIAL_COMMENTS_FOR_PVS_STUDIO
        self.m_extensions = extensions

    @staticmethod
    def IsMatchingFile(file, extensions):
        return file.endswith(tuple(extensions))

    def AddTextToFile(self, filepath):
        with open(filepath, "r") as f:
            content = f.read()

        if self.m_text in content:
            print(DEFAULT_TEXT_ALREADY_PRESENT + filepath)
        else:
            with open(filepath, "w") as f:
                f.write(self.m_text + content)
            print(DEFAULT_TEXT_ADDED + filepath)

    def AddTextToFilesInDirectory(self, directory):
        for root_path, _, files in os.walk(directory):
            matching_files = [file for file in files if TextManipulator.IsMatchingFile(file, self.m_extensions)]
            if not matching_files:
                print(DEFAULT_NO_FILES_WITH_EXTENSIONS_ERROR_MESSAGE + root_path)
                continue

            for file in matching_files:
                filepath = os.path.join(root_path, file)
                self.AddTextToFile(filepath)
