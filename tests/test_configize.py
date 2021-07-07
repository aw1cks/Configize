import pathlib
import textwrap
import unittest

from configize import configize


class TestConfigize(unittest.TestCase):
    def test_path_detection(self):
        pathlib.Path.home().joinpath(".config/test").mkdir(parents=True, exist_ok=True)
        config_path = pathlib.Path.home().joinpath(".config/test/test.yaml")

        with open(config_path, "w") as f:
            pass

        c = configize(Name="test")

        self.assertEqual(config_path, c.path)

        config_path.unlink()

    def test_path_detection_custom(self):
        base_path = pathlib.Path.home().joinpath(".custom")
        base_path.joinpath("test").mkdir(parents=True, exist_ok=True)

        config_path = config_path = base_path.joinpath("test/test.yaml")

        with open(config_path, "w") as f:
            pass

        c = configize(Name="test", Path=str(base_path))

        self.assertEqual(config_path, c.path)

    def test_config_read(self):
        pathlib.Path.home().joinpath(".config/test").mkdir(parents=True, exist_ok=True)
        config_path = pathlib.Path.home().joinpath(".config/test/test.yaml")
        config = """---
        key1: abc
        key2:
          - a
          - b
          - c
        """
        config = textwrap.dedent(config)
        config_dict = {
            "key1": "abc",
            "key2": ["a", "b", "c"],
        }

        with open(config_path, "w") as f:
            f.write(config)

        c = configize(Name="test")

        self.assertEqual(config_dict, c.config)


if __name__ == "__main__":
    unittest.main()
