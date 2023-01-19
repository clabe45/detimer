# Detimer

Detimer is a backup manager that allows you to easily configure backups in a
yaml file and run them. It uses [rdiff-backup](https://rdiff-backup.net) to
perform the backups.

## Overview

A **root** is a backup task, including information such as the directory to back
up, where to store it and exclusion rules.

## Installation

You will need
[rdiff-backup](https://github.com/rdiff-backup/rdiff-backup/releases) installed.
Then you can install detimer:

```
pip install detimer
```

## Usage

```sh
$ detimer -h
Usage: detimer [OPTIONS] COMMAND [ARGS]...

  Simple backup manager

Options:
  -V, --version  Show the version and exit.
  -h, --help     Show this message and exit.

Commands:
  backup  Backup specified roots
  list    List all roots
```

## Configuration

To add a root, edit `config.yml` in:
- OS X: **~/Library/Application Support/Detimer**
- Unix: **~/.config/detimer**
- Windows: **%USERPROFILE%\AppData\Roaming\Detimer**

Each root should have the following properties:
- `name`
- `src` - Absolute path of the source directory
- `dest` - Absolute path of the destination directory
- `match` - Inclusion/exclusion rules. Patterns starting with `-` are excluded,
  and patterns starting with `+` are force-included. Any inclusion lines must
  precede their corresponding exclusion lines (see the example below).

**Example**:

```yml
roots:
  - name: mega
    src: /home/USER
    dest: /mega/backups
    special_files: exclude  # detect|include|exclude
    match: |
      - Downloads
      - **/node_modules
      + another-excluded-dir/except-this-file
      - another-excluded-dir
```

## Contributing

Pull Requests are welcome! Please open an issue before making major changes.
Additionally, we use
[conventional commits](https://www.conventionalcommits.org/en/v1.0.0/).

## License

Licensed under [GNU GPLv3](./LICENSE)
