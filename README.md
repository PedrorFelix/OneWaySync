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

