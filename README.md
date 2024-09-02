# PathUtils

**PathUtils** is a Python package for validating and joining file paths. It provides utility functions to manage and manipulate paths in a simple and Pythonic way.

## Installation

### A. Direct Installation via `pip`

You can install the latest version of **PathUtils** directly from the GitHub repository:

```bash
pip install git+https://github.com/KybraNET/pathutils.git
```

### B. Clone the Repository and Install Locally

If you prefer to clone the repository (e.g., to run tests or contribute), follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/KybraNET/pathutils.git
   cd pathutils
   ```

2. **Set Up a Virtual Environment and Install the Package:**

   - **On macOS/Linux:**

     ```bash
     python3 setup_env.py
     source venv/bin/activate
     ```

   - **On Windows:**

     ```bash
     python3 setup_env.py
     .\venv\Scripts\activate
     ```

## Running Tests

Once you have installed the package in a virtual environment, you can run the tests to ensure everything is working correctly:

```bash
pytest
```

## Usage

Here’s a basic example of how to use **PathUtils**:

```python
from pathutils import validate_and_join_paths, PathError

try:
    # Example 1: Join multiple (Unix-like systems)
    result = validate_and_join_paths("/home/user", "documents", "file.txt")
    print("Joined Path:", result)

    # Example 2: Validate a single path and check if the file exists(Unix-like systems)
    result = validate_and_join_paths("/home/user/documents/file.txt")
    print("Directory Path:", result)
    
    # Example 3: Overwrite an existing file using force 
    result = validate_and_join_paths("home", "user", "documents", "file.txt", force=True)
    print("Overwrite Unix Path with force:", result)

    # Example 4: Join multiple paths (Windows-specific)
    result = validate_and_join_paths("C:", "Users", "YourUsername", "Documents", "file.txt")
    print("Joined Windows Path:", result)

except PathError as e:
    print("Error:", e)
```

### Functions

- **`validate_and_join_paths(*args, force=False)`**:
  - Joins multiple path components and optionally validates the existence of directories or files.
  - **Parameters**:
    - `*args`: Path components to join.
    - `force` (bool): If `True`, allows overwriting an existing file.
  - **Returns**: The resulting path.
  - **Raises**: `PathError` if a path is invalid or a file exists without `force`.

- **`PathError`**:
  - Custom exception raised by the `validate_and_join_paths` function when an error occurs.

## CodeCoverage
```bash
============================= test session starts ==============================
platform linux -- Python 3.10.12, pytest-8.3.2, pluggy-1.5.0
rootdir: /home/dave/Dokumente/GitHub/pathutils
configfile: pyproject.toml
plugins: cov-5.0.0
collected 6 items                                                              

tests/test_path_utils.py ......                                          [100%]

---------- coverage: platform linux, python 3.10.12-final-0 ----------
Name                          Stmts   Miss  Cover   Missing
-----------------------------------------------------------
src/pathutils/__init__.py         3      0   100%
src/pathutils/exceptions.py       2      0   100%
src/pathutils/path_utils.py      15      0   100%
tests/test_path_utils.py         39      0   100%
-----------------------------------------------------------
TOTAL                            59      0   100%


============================== 6 passed in 0.04s ===============================
```

## License

This project is licensed under the LGPLv3 License. See the [LICENSE](LICENSE) file for details.


