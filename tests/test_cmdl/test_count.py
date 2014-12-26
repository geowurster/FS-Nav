"""
FS Nav utility unittests: count
"""


from glob import glob
import unittest

from click.testing import CliRunner

from fsnav import cmdl


class TestCount(unittest.TestCase):

    def setUp(self):
        self.paths = glob('*')
        self.runner = CliRunner()

    def test_unique(self):

        # Count a list of unique paths
        result = self.runner.invoke(cmdl.count.main, self.paths)
        self.assertEqual(0, result.exit_code)
        self.assertEqual(str(len(self.paths)), result.output.strip())

    def test_non_unique(self):

        # Count a list of paths containing duplicates
        paths = self.paths
        paths.append(paths[0])
        paths.append(paths[1])
        result = self.runner.invoke(cmdl.count.main, paths)
        self.assertEqual(0, result.exit_code)
        self.assertEqual(str(len(set(paths))), result.output.strip())

    def test_non_existent(self):

        # Try counting a path that doesn't exist
        result = self.runner.invoke(cmdl.count.main, ['.-1-2-3--I_DONT_EXIST-_-'])
        self.assertEqual(0, result.exit_code)
        self.assertEqual('0', result.output.strip())

    def test_home_dir(self):

        # Home directory path like ~/
        result = self.runner.invoke(cmdl.count.main, ['~/'])
        self.assertEqual(0, result.exit_code)
        self.assertEqual('1', result.output.strip())

    def test_wildcard(self):

        # Wildcard path like *
        result = self.runner.invoke(cmdl.count.main, ['*'])
        self.assertEqual(0, result.exit_code)
        self.assertEqual(str(len(self.paths)), result.output.strip())
