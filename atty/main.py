import os
import pathlib

import click
import rich
import tomli
import tomli_w
from beaupy import select

from atty.version import VERSION

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

ALACRITTY_CONFIG_DIR = pathlib.Path(os.sep.join([str(pathlib.Path.home()), ".config", "alacritty"]))
ALACRITTY_CONFIG_FILE = pathlib.Path(os.sep.join([str(ALACRITTY_CONFIG_DIR), "alacritty.toml"]))
ALACRITTY_THEMES_DIR = pathlib.Path(os.sep.join([str(ALACRITTY_CONFIG_DIR), "themes"]))


console = rich.console.Console()


def _get_theme_file_names(themes_path):
    themes = [f.stem for f in pathlib.Path(themes_path).glob("*.toml")]
    themes.sort()

    return themes


def _get_atty_symlink_path(config):
    return os.sep.join([os.path.dirname(config), "color.toml"])


def _create_symlink(config, themes_dir, theme_selected):
    theme_file = os.sep.join([str(themes_dir), f"{theme_selected}.toml"])

    atty_path = pathlib.Path(_get_atty_symlink_path(config))

    atty_path.unlink(missing_ok=True)
    atty_path.symlink_to(theme_file)


def _update_config(config):
    alacritty_conf_file = str(config)
    alacritty_conf_file_content = {}

    with open(alacritty_conf_file, mode="rb") as fp:
        alacritty_conf_file_content = tomli.load(fp)

    atty_file = _get_atty_symlink_path(config)

    alacritty_conf_file_content["import"] = [atty_file]

    with open(alacritty_conf_file, "wb") as fp:
        tomli_w.dump(alacritty_conf_file_content, fp)


def _set_theme(config, themes_dir, theme_selected):
    _create_symlink(config, themes_dir, theme_selected)
    _update_config(config)


def _theme_selection(config, themes_dir, theme):
    if not theme:
        themes_list = _get_theme_file_names(themes_dir)

        msg = "Up and Down keys: navegate on themes list\nLeft and Right keys: switch page\nESC key: abort\nSelect Color:"

        console.print(msg)

        # Choose one item from a list
        theme = select(themes_list, pagination=True, page_size=10, cursor_style="cyan")

    if theme:
        _set_theme(config, themes_dir, theme)
        console.print(f'The theme "{theme}" has been applied successfully!')


@click.command(context_settings=CONTEXT_SETTINGS)
@click.version_option(VERSION, prog_name="atty")
@click.option(
    "-c",
    "--config",
    default=ALACRITTY_CONFIG_FILE,
    help="Absolute path of Alacritty configuration file",
)
@click.option(
    "-d", "--theme_dir", default=ALACRITTY_THEMES_DIR, help="Absolute path of themes folder"
)
@click.option(
    "-t", "--theme", default=None, help="Select a theme by name instead of showing prompt."
)
def atty(config, theme_dir, theme):
    """
    CLI for Alacritty color theme and configuration switching.

    By default, atty will look for the alacritty's configuration file in
    "$HOME/.config/alacritty/alacritty.toml", for the theme files in "$HOME/.config/alacritty/themes" folder.

    """
    _theme_selection(config, theme_dir, theme)
