from deepdiff import DeepDiff

import pytest
import tomllib

import os

from analisador_sintatico import parser


BASE_PATH: str = "./valid/"



def parse(content: str):

    parser.success = True
    result = parser.parse(content)

    return result if parser.success else "Failed to parse content."


class TestValid:

    @staticmethod
    def get_value_and_expected(filename: str, suite_name: str) -> (dict, dict):

        with open(os.path.join(BASE_PATH, suite_name + "/" + filename)) as file:
            file_content: str = file.read()

        output_dict: dict = parse(file_content)
        expected_dict: dict = tomllib.loads(file_content)

        return output_dict, expected_dict

    @pytest.mark.parametrize("filename", filter(lambda f: f.endswith(".toml"), list(os.listdir(BASE_PATH + "array"))))
    def test_array(self, filename: str):
        print(f"Current file: '{filename}'")
        output, expected_content = self.get_value_and_expected(filename, "array")
        assert DeepDiff(output, expected_content, ignore_order=True) is not None

    @pytest.mark.parametrize("filename", filter(lambda f: f.endswith(".toml"), list(os.listdir(BASE_PATH + "bool"))))
    def test_bool(self, filename: str):
        print(f"Current file: '{filename}'")
        output, expected_content = self.get_value_and_expected(filename, "bool")
        assert DeepDiff(output, expected_content, ignore_order=True) is not None

    @pytest.mark.parametrize("filename", filter(lambda f: f.endswith(".toml"), list(os.listdir(BASE_PATH + "comment"))))
    def test_comment(self, filename: str):
        print(f"Current file: '{filename}'")
        output, expected_content = self.get_value_and_expected(filename, "comment")
        assert DeepDiff(output, expected_content, ignore_order=True) is not None

    @pytest.mark.parametrize("filename",
                             filter(lambda f: f.endswith(".toml"), list(os.listdir(BASE_PATH + "datetime"))))
    def test_datetime(self, filename: str):
        print(f"Current file: '{filename}'")
        output, expected_content = self.get_value_and_expected(filename, "datetime")
        assert DeepDiff(output, expected_content, ignore_order=True) is not None

    @pytest.mark.parametrize("filename", filter(lambda f: f.endswith(".toml"), list(os.listdir(BASE_PATH + "float"))))
    def test_float(self, filename: str):
        print(f"Current file: '{filename}'")
        output, expected_content = self.get_value_and_expected(filename, "float")
        assert DeepDiff(output, expected_content, ignore_order=True) is not None

    @pytest.mark.parametrize("filename",
                             filter(lambda f: f.endswith(".toml"), list(os.listdir(BASE_PATH + "inline-table"))))
    def test_inline_table(self, filename: str):
        print(f"Current file: '{filename}'")
        output, expected_content = self.get_value_and_expected(filename, "inline-table")
        assert DeepDiff(output, expected_content, ignore_order=True) is not None

    @pytest.mark.parametrize("filename", filter(lambda f: f.endswith(".toml"), list(os.listdir(BASE_PATH + "integer"))))
    def test_integer(self, filename: str):
        print(f"Current file: '{filename}'")
        output, expected_content = self.get_value_and_expected(filename, "integer")
        assert DeepDiff(output, expected_content, ignore_order=True) is not None

    @pytest.mark.parametrize("filename", filter(lambda f: f.endswith(".toml"), list(os.listdir(BASE_PATH + "key"))))
    def test_key(self, filename: str):
        print(f"Current file: '{filename}'")
        output, expected_content = self.get_value_and_expected(filename, "key")
        assert DeepDiff(output, expected_content, ignore_order=True) is not None

    @pytest.mark.parametrize("filename", filter(lambda f: f.endswith(".toml"), list(os.listdir(BASE_PATH + "spec"))))
    def test_spec(self, filename: str):
        print(f"Current file: '{filename}'")
        output, expected_content = self.get_value_and_expected(filename, "spec")
        assert DeepDiff(output, expected_content, ignore_order=True) is not None

    @pytest.mark.parametrize("filename", filter(lambda f: f.endswith(".toml"), list(os.listdir(BASE_PATH + "string"))))
    def test_string(self, filename: str):
        print(f"Current file: '{filename}'")
        output, expected_content = self.get_value_and_expected(filename, "string")
        assert DeepDiff(output, expected_content, ignore_order=True) is not None

    @pytest.mark.parametrize("filename", filter(lambda f: f.endswith(".toml"), list(os.listdir(BASE_PATH + "table"))))
    def test_table(self, filename: str):
        print(f"Current file: '{filename}'")
        output, expected_content = self.get_value_and_expected(filename, "table")
        assert DeepDiff(output, expected_content, ignore_order=True) is not None

