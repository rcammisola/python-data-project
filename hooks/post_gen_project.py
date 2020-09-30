import subprocess

project_name = "{{ cookiecutter.project_slug }}"

COMMAND_ACTIVATE_ENV=f"source activate {project_name}"
COMMAND_INSTALL_REPO="pip install -e .[dev]"
COMMAND_INSTALL_PYKERNEL=f"python -m ipykernel install --user --name {project_name} --display-name {project_name}"
COMMAND_RUN_TESTS="invoke tests"

subprocess.run(
    ["conda", "env", "create", "-f", "environment.yml"],
    check=True,
)

subprocess.run(
    f"{COMMAND_ACTIVATE_ENV} && {COMMAND_INSTALL_REPO} && {COMMAND_INSTALL_PYKERNEL} && {COMMAND_RUN_TESTS}",
    check=True,
    shell=True,
)
