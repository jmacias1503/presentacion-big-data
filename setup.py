#!/usr/bin/python3
import os
import subprocess
import sys


def setup():
    # 1. Create the virtual environment
    print("Creating virtual environment...")
    subprocess.run([sys.executable, "-m", "venv", "venv"])

    # 2. Determine the path to the python executable inside the venv
    if sys.platform == "win32":
        python_executable = os.path.join("venv", "Scripts", "python.exe")
    else:
        python_executable = os.path.join("venv", "bin", "python")

    # 3. Install requirements
    print("Installing requirements...")
    subprocess.run([python_executable, "-m", "pip",
                   "install", "--upgrade", "pip"])
    if os.path.exists("requirements.txt"):
        subprocess.run([python_executable, "-m", "pip",
                       "install", "-r", "requirements.txt"])

    print("\nSetup complete! To activate your environment:")
    if sys.platform == "win32":
        print("    venv\\Scripts\\activate")
    else:
        print("    source venv/bin/activate")


if __name__ == "__main__":
    setup()
