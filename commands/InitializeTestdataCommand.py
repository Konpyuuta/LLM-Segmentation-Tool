'''

@author Maurice Amon
'''
from commands.Command import Command
import os

class InitializeTestdataCommand(Command):

    _sourcecode_list = None

    _test_dir_path = None

    def __init__(self, test_dir_path):
        self._test_dir_path = test_dir_path
        self._sourcecode_list = list()


    def execute(self):
        for file in os.listdir(self._test_dir_path):
            absolute_path = os.path.join(self._test_dir_path, file)
            if os.path.isfile(absolute_path):
                with open(absolute_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self._sourcecode_list.append((file, content))


    def get_source_files(self):
        return self._sourcecode_list