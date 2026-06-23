# OneWaySync

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A light python CLI tool that was written in order to synchronize two folders: source and replica. 

### Full Folder Replication
- The program maintains a full, identical copy of a designated source folder at a destination folder.

### Automatically Runs Periodically
- This script executes periodically, allowing the user to set the frequency.

### Everything Logged
- Logs are kept in user specified files and cli, allowing complete transparency.

### User Privacy
- No third-party dependencies, runs entirely on Python's standard library. User data is kept completely in user control.


## Requirements
- **OS:** Linux, Windows, MacOS
- **Python:** Version 3.8+

## Installation

No external installation is required! This utility runs completely on Python's native libraries.

```bash
# Clone the repository
git clone https://github.com/PedrorFelix/OneWaySync.git
cd OneWaySync

# verify your Python version (requires 3.8+)
python --version
```

## Usage
### Command Line Parameters

| Short | Long | Description | Required |
| :--- | :--- | :--- | :--- |
| `-s` | `--source` | Absolute path to the source folder. | **Yes** |
| `-r` | `--replica` | Absolute path to the replica/destination folder. | **Yes** |
| `-l` | `--log` | Absolute path to the target log file. | **Yes** |
| `-f` | `--frequency` | Time interval between synchronizations (in seconds). | **Yes** |

### Example

```bash
python sync.py -s /path/to/source/folder -r /path/to/replica/folder -l /path/to/log/file.txt -f 60
```
