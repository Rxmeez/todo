import sys
from subprocess import CalledProcessError, check_call

def _check_call_quiet(commands: list[str]) -> None:
    try:
        check_call(commands)
    except CalledProcessError as error:
        sys.exit(error.returncode)
def format() -> None:
    _check_call_quiet(["black", "--check", "--diff", "src/", "tests/"])
    _check_call_quiet(["isort", "--check", "--diff", "src", "tests"])

def reformat() -> None:
    _check_call_quiet(["black", "src/", "tests/"])
    _check_call_quiet(["isort", "src", "tests"])
    
def lint() -> None:
    _check_call_quiet(["mypy", "src/backend/", "tests/"])
    _check_call_quiet(["flake8", "src/", "tests/"])
    _check_call_quiet(["vulture", "src/"])
    _check_call_quiet(["bandit", "-r", "src/"])
    
def test() -> None:
    _check_call_quiet(["pytest", "tests/", *sys.argv[1:]])