# Detimer

Detimer provides a high-level interface for making backups. Say goodbye to messy
backup scripts. With this tool you can configure all your backup targets in a
single yaml file.

**Currently supported backup tools:**
- [rdiff-backup](https://rdiff-backup.net)
- *more coming soon*

## Overview

A **root** is a backup job, including information such as the directory to back
up, where to store it and exclusion rules. Eventually, you will also be able to
specify a backup tool (for now rdiff-backup is assumed).

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

  Universal backup manager

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
