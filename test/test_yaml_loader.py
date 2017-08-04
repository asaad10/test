import unittest2
import yamlloader

# import the antigravity module
from yamlloader import yaml_loader

class TestYamlLoader(unittest2.TestCase):
    def setUp(self):
        yl = yaml_loader.YamlLoader('amr','saad')
        self.name = yl.get_full_name()
    def tearDown(self):
        pass
    def test_name(self):
        self.assertEquals(self.name, 'amrsaad')
    def test_name_fail(self):
        self.assertEquals(self.name,'fake')

