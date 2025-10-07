"""
setup_s4.py
Installs S4_Slicer and its dependencies on Windows.

Requires Python 3.12, install from https://www.python.org/downloads/windows.
Requires Git for Windows, install from https://git-scm.com/download/win.
Run "py -3.12 setup_s4.py" in the command line.

University of Georgia - Jacob Navarrete, 2025
"""

import venv
import subprocess
import sys
import os
import shutil

# Create a virtual environment  
def create_virtual_env(env_name):
    venv.create(env_name, with_pip=True)
    print(f"[-] Virtual environment '{env_name}' created.")

def check_git_installed():
    try:
        subprocess.run(["git", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("[-] Git is installed.")
    except subprocess.CalledProcessError:
        print("[!] Git is not installed. Please install Git for Windows from https://git-scm.com/download/win.")
        exit(1)

def check_python_version():
    version = sys.version_info
    if version.major != 3 or version.minor < 12:
        print("[!] Python 3.12 is required. Please install it from https://www.python.org/downloads/windows.")
        exit(1)
    else:
        print(f"[-] Python version {sys.version_info.major}.{sys.version_info.minor} is sufficient.")

def clone_repo(repo_url, clone_dir):
    try:
        subprocess.run(["git", "clone", repo_url, clone_dir], check=True)
        print(f"[-] Cloned repository from {repo_url} to {clone_dir}.")
    except subprocess.CalledProcessError as e:
        if "already exists" in str(e):
            print(f"[!] Directory '{clone_dir}' already exists. Please remove it or choose a different location.")

def replace_main_notebook():
    edited_notebook = "main.ipynb"
    original_notebook = os.path.join("S4_Slicer", "main.ipynb")
    shutil.copy(edited_notebook, original_notebook)
    print(f"[-] Replaced {original_notebook}.")

if __name__ == "__main__":
    check_python_version()
    check_git_installed()
    create_virtual_env(".venv")
    clone_repo("https://github.com/jyjblrd/S4_Slicer.git", "S4_Slicer") 
    replace_main_notebook()
    print("Setup complete. Please activate the virtual environment and install dependencies as needed.")