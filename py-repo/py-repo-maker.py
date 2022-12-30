import glob, readline

from os import makedirs, system, listdir
from shutil import copyfile
from os.path import abspath, join, isdir, basename, isfile, dirname

# Setup the teriminal autocomplete
# ------------------------------------------------------------------------------------------
def complete(text, state):
    return (glob.glob(text + "*") + [None])[state]


readline.set_completer_delims(" \t\n;")
readline.parse_and_bind("tab: complete")
readline.set_completer(complete)
# ------------------------------------------------------------------------------------------

# Define the path python utils folder
utils_path = join(dirname(abspath(__file__)), "utils")

# Ask the user for input
system("clear")
print("-----------------------------------------------------------------------------------")
print("                   GitHub repository setup tool: Python 3")
print("-----------------------------------------------------------------------------------")
path = input("Select the path to the empty repository folder: ")
path = abspath(path)
name = basename(path)

if not isdir(path):
    print("ERROR: the selected repository path is not valid")
    exit()

author = input("Select the author name: ")
description = input("Enter a single line description of the package: ")

if input("Would you like to provide a requirements.txt file (y/n): ").upper() == "Y":
    requirement_path = input("Select the path to requirements.txt file: ")
    copyfile(requirement_path, join(path, "requirements.txt"))

elif not isfile(join(path, "requirements.txt")):
    with open(join(path, "requirements.txt"), "w") as file:
        pass

# Copy the base files in the repository folder
copyfile(join(utils_path, "requirements-dev.txt"), join(path, "requirements-dev.txt"))
copyfile(join(utils_path, "tox.ini"), join(path, "tox.ini"))
copyfile(join(utils_path, "setup.py"), join(path, "setup.py"))
copyfile(join(utils_path, "pyproject.toml"), join(path, "pyproject.toml"))

with open(join(path, "setup.cfg"), "w") as sfile:
    sfile.write(
        f"""
[metadata]
name = {name}
description = {description}
author = {author}
platforms = unix, linux
classifiers =
    Programming Language :: Python :: 3.8
    Programming Language :: Python :: 3.9
    Programming Language :: Python :: 3.10

[options]
packages =
    {name.lower()}
install_requires =
        """
    )

    with open(join(path, "requirements.txt"), "r") as rfile:
        for line in rfile:
            sfile.write(f"\t{line}")

    sfile.write(
        f"""
python_requires = >=3.8
package_dir =
    =src
zip_safe = no

[options.extras_require]
testing =
"""
    )

    with open(join(path, "requirements-dev.txt"), "r") as rfile:
        for line in rfile:
            sfile.write(f"\t{line}")

    sfile.write(
        f"""

[flake8]
max-line-length = 100
        """
    )

# Create a src folder containing the library code
src_path = join(path, f"src/{name.lower()}")
makedirs(src_path, exist_ok=True)
if not isfile(join(src_path, "__init__.py")):
    with open(join(src_path, "__init__.py"), "w") as file:
        pass

# Create a tests folder
makedirs(join(path, "tests"), exist_ok=True)

# Create a docs folder and copy the required files into it
docs_path = join(path, "docs")
makedirs(docs_path, exist_ok=True)
for filename in listdir(join(utils_path, "docs")):
    copyfile(join(utils_path, f"docs/{filename}"), join(docs_path, filename))


# Create a .github folder
workflows_path = join(path, ".github/workflows")
makedirs(workflows_path, exist_ok=True)
copyfile(join(utils_path, "docs-deploy.yml"), join(workflows_path, "docs-deploy.yml"))
copyfile(join(utils_path, "tests.yml"), join(workflows_path, "tests.yml"))
