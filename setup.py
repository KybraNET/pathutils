from setuptools import setup, find_packages
import os

def create_directories():
    """Function to create necessary directories if they don't exist."""
    dirs = ['src/pathutils', 'tests']
    for dir in dirs:
        os.makedirs(dir, exist_ok=True)

    with open(os.path.join('src/pathutils', '__init__.py'), 'w') as f:
        f.write("from .path_utils import validate_and_join_paths\nfrom .exceptions import PathError\n\n__all__ = ['validate_and_join_paths', 'PathError']\n")
    
    with open(os.path.join('src/pathutils', 'path_utils.py'), 'w') as f:
        f.write('''import os\nfrom .exceptions import PathError\n\ndef validate_and_join_paths(*args, force=False):\n    """\n    Validates and joins path components.\n\n    - If two or more arguments are provided, checks if the first is a directory.\n    - If one argument is provided, checks if it's a valid path and handles file existence based on the `force` flag.\n    \n    Parameters:\n        *args: Path components to be joined.\n        force (bool): If True, allows overwriting existing files.\n\n    Returns:\n        str: The resulting path or directory.\n\n    Raises:\n        PathError: If the provided paths are invalid or a file exists without `force`.\n    """\n    if len(args) >= 2:\n        if not os.path.isdir(args[0]):\n            raise PathError(f"The first argument is not a valid directory: {args[0]}")\n        return os.path.join(*args)\n    elif len(args) == 1:\n        full_path = args[0]\n        directory, filename = os.path.split(full_path)\n        if not os.path.isdir(directory):\n            raise PathError(f"The directory does not exist: {directory}")\n        if os.path.isfile(full_path) and not force:\n            raise PathError(f"The file '{filename}' already exists in '{directory}'.")\n        return directory\n    else:\n        raise PathError("At least one argument is required.")\n''')

    with open(os.path.join('src/pathutils', 'exceptions.py'), 'w') as f:
        f.write('''class PathError(Exception):\n    """Custom exception for path-related errors."""\n    pass\n''')

    with open(os.path.join('tests', 'test_path_utils.py'), 'w') as f:
        f.write('''import os\nimport unittest\nfrom pathutils.path_utils import validate_and_join_paths\nfrom pathutils.exceptions import PathError\n\nclass TestValidateAndJoinPaths(unittest.TestCase):\n    @classmethod\n    def setUpClass(cls):\n        cls.base_dir = os.getcwd()\n        cls.test_file = os.path.join(cls.base_dir, 'test_file.txt')\n        with open(cls.test_file, 'w') as f:\n            pass\n\n    @classmethod\n    def tearDownClass(cls):\n        if os.path.isfile(cls.test_file):\n            os.remove(cls.test_file)\n\n    def test_multiple_arguments_valid_directory(self):\n        result = validate_and_join_paths(self.base_dir, 'subdir', 'file.txt')\n        expected = os.path.join(self.base_dir, 'subdir', 'file.txt')\n        self.assertEqual(result, expected)\n\n    def test_multiple_arguments_invalid_directory(self):\n        with self.assertRaises(PathError):\n            validate_and_join_paths('/invalid/path', 'file.txt')\n\n    def test_single_argument_valid_path_file_does_not_exist(self):\n        new_file = os.path.join(self.base_dir, 'new_file.txt')\n        result = validate_and_join_paths(new_file)\n        self.assertEqual(result, self.base_dir)\n\n    def test_single_argument_valid_path_file_exists(self):\n        with self.assertRaises(PathError):\n            validate_and_join_paths(self.test_file)\n\n    def test_single_argument_valid_path_file_exists_force(self):\n        result = validate_and_join_paths(self.test_file, force=True)\n        self.assertEqual(result, self.base_dir)\n\n    def test_no_arguments(self):\n        with self.assertRaises(PathError):\n            validate_and_join_paths()\n\n    def test_first_argument_is_not_a_directory(self):\n        with self.assertRaises(PathError):\n            validate_and_join_paths(self.test_file, 'file.txt')\n\n    def test_force_overwrite_file(self):\n        with open(self.test_file, 'w') as f:\n            f.write('Initial content')\n        result = validate_and_join_paths(self.test_file, force=True)\n        self.assertEqual(result, self.base_dir)\n        with open(self.test_file, 'r') as f:\n            content = f.read()\n        self.assertEqual(content, 'Initial content')\n\nif __name__ == '__main__':\n    unittest.main()\n''')

create_directories()

setup(
    name="pathutils",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    extras_require={
        "dev": [
            "pytest",
            "black",
        ],
    },
    tests_require=["unittest"],
    description="A Python package for validating and joining paths.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="KybraNET",
    url="https://github.com/KybraNET/pathutils",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
