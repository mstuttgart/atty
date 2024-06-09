import glob
import os
from pathlib import Path

import click
import rich
import tomli
import tomli_w
from beaupy import select

from atty.version import VERSION

console = rich.console.Console()

ALACRITTY_CONFIG_DIR = ".config/alacritty"
ALACRITTY_CONFIG_FILE = f"{ALACRITTY_CONFIG_DIR}/alacritty.toml"
ALACRITTY_THEME_DIR = f"{ALACRITTY_CONFIG_DIR}/themes/themes"
ATTY_FILE = f"{ALACRITTY_CONFIG_DIR}/atty.toml"


def _get_theme_file_names():

    themes = glob.glob(os.sep.join([f"{ALACRITTY_THEME_DIR}", "*.toml"]))

    themes = [
        "everforest_dark",
        "everforest_light",
        "rose-pine-dawn",
        "rose-pine-moon",
    ]

    return themes


def _create_symlink(theme):
    atty_file = os.sep.join([str(Path.home()), f"{ATTY_FILE}"])
    theme_path = os.sep.join([str(Path.home()), f"{ALACRITTY_THEME_DIR}", f"{theme}.toml"])

    atty_path = Path(atty_file)

    atty_path.unlink(missing_ok=True)

    atty_path.symlink_to(theme_path)


def _update_config():

    alacritty_conf_path = os.sep.join([str(Path.home()), ALACRITTY_CONFIG_FILE])
    alacritty_conf = {}

    with open(alacritty_conf_path, mode="rb") as fp:
        alacritty_conf = tomli.load(fp)

    atty_file = os.sep.join([str(Path.home()), f"{ATTY_FILE}"])

    alacritty_conf["import"] = [atty_file]

    with open(alacritty_conf_path, "wb") as fp:
        tomli_w.dump(alacritty_conf, fp)


def _set_theme(theme):
    _create_symlink(theme)
    _update_config()


@click.command("atty")
@click.version_option(VERSION, prog_name="atty")
def cli():
    themes = _get_theme_file_names()
    console.print("Select a theme")

    # Choose one item from a list
    theme = select(themes, cursor="🢧", cursor_style="cyan")
    _set_theme(theme)
    console.print(f'The theme "{theme}" has been applied successfully!')


if __name__ == "__main__":
    cli()
