import unittest
from os import path, system
from sources import controller


class TestModelClass(unittest.TestCase):

    terminal_colors = {
        'OKBLUE': '\033[94m',
        'ENDC': '\033[0m'
    }

    # def test_config_creation_if_not_exists(self):
    #     if path.exists('../config.txt'):
    #         system('rm ../config.txt')
    #
    #     if path.exists('../config.txt'):
    #         raise FileExistsError('File config.txt could not be removed.')
    #
    #     test_controller = controller.Controller()
    #     self.assertTrue(path.exists('../config.txt'), 'File config.txt not created by controller')
    def test_config_creation_if_not_exists(self):
        if path.exists('config.txt'):
            system('rm config.txt')

        if path.exists('../config.txt'):
            raise FileExistsError('File config.txt could not be removed.')

        print(f'{self.terminal_colors["OKBLUE"]}Please close app window to complete test.{self.terminal_colors["ENDC"]}')
        test_controller = controller.Controller()
        del test_controller
        self.assertTrue(path.exists('config.txt'), 'File config.txt not created by controller')
