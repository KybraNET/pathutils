import os
import subprocess
import sys

def create_virtualenv():
    """Create a virtual environment in the current directory."""
    venv_dir = os.path.join(os.getcwd(), 'venv')

    # Check if venv already exists
    if not os.path.isdir(venv_dir):
        print("Creating virtual environment...")
        subprocess.check_call([sys.executable, '-m', 'venv', 'venv'])
    else:
        print("Virtual environment already exists.")

def install_packages():
    """Activate the virtual environment and install packages."""
    print("Installing packages...")
    
    # Determine the correct pip executable to use
    if os.name == 'nt':  # Windows
        pip_executable = os.path.join('venv', 'Scripts', 'pip')
    else:  # macOS/Linux
        pip_executable = os.path.join('venv', 'bin', 'pip')

    # Upgrade pip and install the package with development dependencies
    subprocess.check_call([pip_executable, 'install', '--upgrade', 'pip'])
    subprocess.check_call([pip_executable, 'install', '-e', '.[dev]'])

def main():
    create_virtualenv()
    install_packages()

if __name__ == "__main__":
    main()
