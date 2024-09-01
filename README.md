# PathUtils

**PathUtils** is a Python package for validating and joining file paths. It provides utility functions to manage and manipulate paths in a simple and Pythonic way.

## Installation

### A. Direct Installation via `pip`

You can install the latest version of **PathUtils** directly from the GitHub repository:

```bash
pip install git+https://github.com/johndoe/pathutils.git
```

### B. Clone the Repository and Install Locally

If you prefer to clone the repository (e.g., to run tests or contribute), follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/johndoe/pathutils.git
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
    # Example 1: Join multiple paths
    result = validate_and_join_paths("/home/user", "documents", "file.txt")
    print("Joined Path:", result)

    # Example 2: Validate a single path and check if the file exists
    result = validate_and_join_paths("/home/user/documents/file.txt")
    print("Directory Path:", result)

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

## License

This project is licensed under the LGPLv3 License. See the [LICENSE](LICENSE) file for details.


