import sys


def return_python_interpreter_version() -> str:
    python_interpreter_version: str = sys.version
    return python_interpreter_version


def print_python_interpreter_version() -> None:
    python_interpreter_version: str = return_python_interpreter_version()
    f_python_interpreter_version: str = f'Python interpreter version is: {python_interpreter_version}'
    print(f_python_interpreter_version)
