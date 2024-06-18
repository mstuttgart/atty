import os

from atty.main import _create_symlink, _get_atty_symlink_path, _get_theme_file_names

test_folder_dir = os.path.dirname(os.path.abspath(__file__))


def test__get_atty_symlink_path():
    config = ".config/alacritty/alacritty.toml"
    res = _get_atty_symlink_path(config)
    assert res == ".config/alacritty/color.toml"


def test__get_theme_file_names():
    themes_path = f"{test_folder_dir}/.config/alacritty/themes"
    themes_filename = _get_theme_file_names(themes_path)

    assert themes_filename == ["t1", "t2", "t3"]


def test__create_symlink():
    config_file = os.sep.join([test_folder_dir, ".config", "alacritty", "alacritty.toml"])
    themes_path = os.sep.join([test_folder_dir, ".config", "alacritty", "themes"])
    theme_selected = "t3"

    _create_symlink(config_file, themes_path, theme_selected)

    symlink_file = os.sep.join([test_folder_dir, ".config", "alacritty", "color.toml"])
    assert os.path.exists(symlink_file)
    assert os.path.islink(symlink_file)
