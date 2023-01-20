# Detimer

Detimer is a backup manager that allows you to easily configure backups in a
yaml file and run them. It uses [rdiff-backup](https://rdiff-backup.net) to
perform reverse differential backups.

:warning: **This project is still in early development and is not ready for
production use.**

## Features

- [x] Configure backup tasks in a yaml file
- [x] Create backups
- [x] Compression of backup files and transfer over SSH (provided by
      rdiff-backup)
- [ ] Restore backups
- [ ] List backups
- [ ] Delete backups
- [ ] Schedule backups

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

Each root can have the following properties:
- `name` (required) - Name of the root
- `src` (required) - Absolute path of the source directory
- `dest` (required) - Absolute path of the destination directory
- `special_files` - How to handle special files (e.g. symlinks, devices, etc.)
  - `detect` - Let rdiff-backup decide based on the OS (default)
  - `include` - Include special files in the backup
  - `exclude` - Exclude special files from the backup
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
