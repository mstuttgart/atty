import nox

nox.options.sessions = ["tests", "lint"]


@nox.session
def tests(session: nox.Session) -> None:
    """
    Run the unit and regular tests.
    """
    session.install("-e.[dev]")
    session.run("pytest", "-v", "--color=yes", "tests/", "atty/")


@nox.session
def lint(session: nox.Session) -> None:
    """
    Run lint.
    """
    session.install("-e.[dev]")
    session.run("ruff", "check", "atty/")
    session.run("black", "--check", "atty/")
    session.run("isort", "--check", "atty/")


@nox.session
def coverage(session: nox.Session) -> None:
    """
    Run coverage.
    """
    session.install("-e.[coverage]")
    session.run("pytest", "--cov", "atty")
