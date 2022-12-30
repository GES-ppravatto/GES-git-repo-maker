# GES-git-repo-maker
This repository contain simple tools to help the user in the setup of a GitHub repository. The tool is written in python3 and is compatible only with linux based machines.

At this version the following configurations are available:
* Setup of a `python3` repository matching the [`pip` standard format](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

#### Requirements
To follow the tutorials presented in what follows, you should meet the following requirements:
* python >= 3.8
* git

## Download of the tool
The tool can be downloaded by cloning this repository. This can be done using the command:
```
git clone https://github.com/GES-ppravatto/GES-git-repo-maker
```
The tool can be copied in any path on your machine. In what follows we will use the symbol `<tool_path>` to indicate the path to the `GES-git-repo-maker` folder.

## Setup of a new `python3` PyPI package repository

To setup a python3 repository formatted according to the `PyPI` package standard you can proceed as follows:
* Create a repository on GitHub and clone in on your local machine using the `git clone <repo-url>` command. We will call the path to the repository as `<target_path>`.
* Run the `py-repo-maker` tool using the command: `python3 <tool_path>/py-repo/py-repo-maker.py`. This will clear your terminal and display a terminal based user interface.
* Enter all the required data such as the path to the repository folder (`<target_path>`), your name and a single line description of the package
* (optional) If your repository already has defined requirements you can provide the path to a `requirements.txt` file that will be included in the final file tree.
* Once the repository has been configured proceed to manually fulfill the following tasks:
  * Add the python scripts to the `src/<package-name>` folder (remember to ad an `__init__.py` file)
  * Add tests to the `tests` folder
  * Update/modify the minimal documentation created in `docs`

**Warning**: The repository already contains all the workflows necessary to run the tests using `tox` and to build and deploy the documentation on GitHub pages using `jupyter-books`. Please make sure that at least a minimal test is provided in the test folder and make sure that the deploy to `gh-pages` is enabled in your repository to avoid GitHub action failure.