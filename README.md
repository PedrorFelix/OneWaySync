# OneWaySync

This script has the objective of implementing a program that synchronizes two folders: source and
replica. The program should maintain a full, identical copy of source
folder at replica folder.

## Considerations

- The script must be written in Python;
- Synchronization must be one-way from source to replica;
- Synchronization should be performed periodically;
- Third-party libraries should be limited to well known algorithms and not include any libaries that implement synchonization of folders;
- File creation, copying and removal operations should be logged to a file and to the console output;
- The script must take multiple command line arguments that define the folders paths, the interval between synchronazations and the log file path.

## Usage
### Parameters

All parameters defined in this list are required for the script to run

-s, --source : The absolute path to the source folder

-r, --replica : The absolute path to the replica folder

-l, --log : The absolute path to the file to be used as log

-f, --frequency : The amount of seconds that shoud pass between synchronizations

### Example

```bash
> python sync.py -s /path/to/source/folder -r /path/to/replica/folder -l /path/to/log/file.txt -f 60
```
