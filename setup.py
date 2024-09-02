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
        f.write('''import os\nfrom .exceptions import PathError\n\ndef validate_and_join_paths(*args, force=False):\n    """\n    Validates and joins path components.\n\n    - If multiple arguments are provided, they are joined into a single path.\n    - Checks if the directory part of the path exists.\n    - If a file exists at the final path, raises an error unless `force` is True.\n\n    Parameters:\n        *args: Path components to be joined.\n        force (bool): If True, allows overwriting existing files.\n\n    Returns:\n        str: The resulting path.\n\n    Raises:\n        PathError: If the provided paths are invalid or a file exists without `force`.\n        ValueError: If no path components are provided.\n    """\n    if not args:\n        raise ValueError("At least one argument is required.")\n\n    # Join all path components into a full path\n    full_path = os.path.join(*args)\n    directory, filename = os.path.split(full_path)\n\n    # Only check the directory part if it's not empty\n    if directory and not os.path.isdir(directory):\n        raise PathError(f"The directory \'{directory}\' does not exist.")\n\n    # Check if the final path exists\n    if os.path.exists(full_path):\n        # If it\'s a file, raise an error unless force is True\n        if os.path.isfile(full_path) and not force:\n            raise PathError(f"The file \'{filename}\' already exists in \'{directory}\'.")\n        # If it\'s a directory and no more components follow, return the directory\n        elif os.path.isdir(full_path) and len(args) == 1:\n            return full_path\n    \n    return full_path\n''')

    with open(os.path.join('src/pathutils', 'exceptions.py'), 'w') as f:
        f.write('''class PathError(Exception):\n    """Custom exception for path-related errors."""\n    pass\n''')

    with open(os.path.join('tests', 'test_path_utils.py'), 'w') as f:
        f.write('''import os\nimport unittest\nfrom pathutils.path_utils import validate_and_join_paths\nfrom pathutils.exceptions import PathError\nfrom pathlib import Path\n\nclass TestValidateAndJoinPaths(unittest.TestCase):\n\n    @classmethod\n    def setUpClass(cls):\n        cls.base_dir = os.getcwd()\n        cls.existing_dir = os.path.join(cls.base_dir, \'existing_dir\')\n        cls.existing_file = os.path.join(cls.existing_dir, \'existing_file.txt\')\n\n        # Set up a directory and a file to test against\n        os.makedirs(cls.existing_dir, exist_ok=True)\n        with open(cls.existing_file, \'w\') as f:\n            f.write(\'Test content\')\n\n        # Use the user\'s home directory directly\n        cls.user_home_dir = Path.home()  # Dynamically gets the user\'s home directory\n\n    @classmethod\n    def tearDownClass(cls):\n        if os.path.isfile(cls.existing_file):\n            os.remove(cls.existing_file)\n        if os.path.isdir(cls.existing_dir):\n            os.rmdir(cls.existing_dir)\n\n    def test_join_multiple_paths(self):\n        result = validate_and_join_paths(self.user_home_dir, \'file.txt\')\n        self.assertEqual(result, os.path.join(self.user_home_dir, \'file.txt\'))\n\n    def test_directory_does_not_exist(self):\n        with self.assertRaises(PathError):\n            validate_and_join_paths(\'/non/existent/directory\', \'file.txt\')\n\n    def test_file_exists_without_force(self):\n        with self.assertRaises(PathError):\n            validate_and_join_paths(self.existing_dir, \'existing_file.txt\')\n\n    def test_file_exists_with_force(self):\n        result = validate_and_join_paths(self.existing_dir, \'existing_file.txt\', force=True)\n        self.assertEqual(result, self.existing_file)\n\n    def test_return_existing_directory(self):\n        result = validate_and_join_paths(self.existing_dir)\n        self.assertEqual(result, self.existing_dir)\n\n    def test_no_arguments(self):\n        with self.assertRaises(ValueError):\n            validate_and_join_paths()\n\nif __name__ == \'__main__\':  # pragma: no cover\n    unittest.main()  # pragma: no cover\n''')

create_directories()

setup(
    name="pathutils",
    version="0.1.1",
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
        "License :: OSI Approved :: LGPLv3 License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
