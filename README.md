<h2 align="center">
  <a href="https://pypi.org/project/atty/">
    <img src="https://github.com/mstuttgart/atty/assets/8174740/2ce05801-e28a-470c-b755-68081671344f" width="15%">
  </a>
  <br>
      Atty
</h2>

<p align="center">

  <a href="https://github.com/mstuttgart/atty/actions/workflows/test.yml">
    <img alt="GitHub Workflow Status" src="https://github.com/mstuttgart/atty/actions/workflows/test.yml/badge.svg">
  </a>

  <a href="https://codecov.io/gh/mstuttgart/atty">
     <img alt="Codecov" src="https://img.shields.io/codecov/c/github/mstuttgart/atty?color=fcd800">
  </a>

  <a href="https://pypi.org/project/atty">
    <img src="https://img.shields.io/pypi/dm/atty?color=fcd800" alt="Downloads">
  </a>

  <a href="https://pypi.org/project/atty">
    <img src="https://img.shields.io/pypi/v/atty.svg?" alt="Ratings">
  </a>

  <a href="https://pypi.org/project/atty/">
    <img src="https://img.shields.io/pypi/pyversions/atty.svg" alt="Version">
  </a>

</p>

<p align="center">
  <a href="#about">About</a> |
  <a href="#install">Install</a> |
  <a href="#how-to-use">How to Use</a> |
  <a href="#configuration">Configuration</a> |
  <a href="#contribute">Contribute</a>
</p>

## About

`Atty` is a `cli` utility for [Alacritty](https://github.com/alacritty/alacritty) color theme switching.

> [!NOTE]
> This hasn't been tested on Windows and OS X yet. There'll probably be issues with default settings, as it's looking for the `$HOME/.config/alacritty` folder, but after setting the `--config` and `--theme_dir` flags, it should work just fine.

## Install

The recommended way to get _atty_ is to **install the latest stable release**:

```sh
pip install atty
```

or using [pipx](https://github.com/pypa/pipx):

```sh
pipx install atty
```

## How to Use

The default themes folder is in `$HOME/.config/alacritty/themes/`.

Example:

```
.
├── alacritty
│   ├── alacritty.yml
│   └── themes
```

> [!TIP]
> You can get the oficial themes repository of `alacritty`:
>
> `git clone git@github.com:alacritty/alacritty-theme.git $HOME/.config/alacritty/themes/`

Next, run `atty` and select you favority theme:

> atty

```sh
Up and Down keys: navegate on themes list
Left and Right keys: switch page
ESC key: abort
Select Color:
> Cobalt2
  Mariana
  afterglow
  alabaster
  alabaster_dark
  argonaut
  atom_one_light
  ayu_dark
  ayu_light
  baitong

Page 1/11

(enter to confirm)
```

## Configuration

The utility can be configured by passing additional flags/parameters:

```sh
aty --help

Usage: atty [OPTIONS]

  CLI for Alacritty color theme and configuration switching.

  By default, atty will look for the alacritty's configuration file in
  "$HOME/.config/alacritty/alacritty.toml", for the theme files in
  "$HOME/.config/alacritty/themes" folder.

Options:
  --version             Show the version and exit.
  -c, --config TEXT     Absolute path of Alacritty configuration file
  -d, --theme_dir TEXT  Absolute path of themes folder
  -t, --theme TEXT      Select a theme by name instead of showing prompt.
  -h, --help            Show this message and exit.
```


## Contribute

See this *guideline* [here](https://github.com/mstuttgart/atty/blob/main/.github/CONTRIBUTING.md).
