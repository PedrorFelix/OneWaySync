import argparse
import os
from sys import exit
from time import sleep
from datetime import datetime
from pathlib import Path
import filecmp
import shutil

def log(file, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    final_message = timestamp + " - " + message + "\n"
    log = Path(file)
    log.open('w').write(final_message)
    print(final_message)

def sync_additions(source_path, replica_path, logfile):
    for item in os.listdir(source_path):
        sourceEntry = os.path.join(source_path, item)
        replicaEntry = os.path.join(replica_path, item)

        if os.path.isdir(sourceEntry):
            if  not os.path.exists(replicaEntry):
                log(logfile, "Creating " + item + " at " + replica_path)
                os.makedirs(replicaEntry)
                sync_additions(sourceEntry, replicaEntry, logfile)
        else:
            if not os.path.exists(replicaEntry) or not filecmp(sourceEntry, replicaEntry):
                log(logfile, "Copying " + item + " into " + replica_path)
                shutil.copy2(sourceEntry, replicaEntry) #copy2 attempts to perserve metadata

    log(logfile, "Finished adding new content to replica folder")

def sync_deletions(source_path, replica_path, logfile):
    for item in os.listdir(replica_path):
        sourceEntry = os.path.join(source_path, item)
        replicaEntry = os.path.join(replica_path, item)

        if not os.path.exists(sourceEntry):
            if os.path.isdir(sourceEntry):
                log(logfile, "Deleting Folder" + item + " from " + replica_path)
                shutil.rmtree(replicaEntry)
            else:
                log(logfile, "Deleting File" + item + " from " + replica_path)
                os.remove(replicaEntry)

    log(logfile, "Finished cleaning deleted content from replica folder")

def sync(source_path, replica_path, file):
    log(file, "Beggining Synchonization by adding new content to replica folder")
    sync_additions(source_path, replica_path, file)
    log(file, "Cleaning deleted source files from replica folder")
    sync_deletions(source_path, replica_path, file)
    log(file, "Finished Synchonization")

def main():
    parser = argparse.ArgumentParser(description="Replicates a source folder frequently")
    parser.add_argument("-s", "--source", help="Path of the folder to be replicated", required=True)
    parser.add_argument("-r", "--replica", help="Path of the replica folder", required=True)
    parser.add_argument("-l", "--log", help="Path of the log file", required=True)
    parser.add_argument("-f", "--frequency", help="frequency with witch the replication must occur", required=True)
    args = parser.parse_args()

    print(f"arguments:\nsource: {args.source},\nreplica: {args.replica},\nlog: {args.log},\nfrequency: {args.frequency}")

    try:
        frequency = int(args.frequency)
    except ValueError:
        print("Invalid Frequency (Must be a numeric value)")
        exit(1)

    if os.path.exists(args.source):
        source = args.source
        if os.path.exists(args.replica):
            replica = args.replica
    else:
        print("Source folder does not exist")
        exit(1)

    if os.path.isfile(args.log):
        logfile = args.log
    else:
        print("Log file given is not valid")
        answer = input("Should a log file be created at replica folder? (y/n)").strip().lower()
        if answer == 'y':
            print(f"Creating a log file at {args.replica}")
            logfile= os.path.join(replica, "logfile.txt")
            Path(logfile).touch()
        else:
            print("Please insert a valid log file")
            exit(1)

    try:
        while True:
            print("Running the Script. Press Ctrl+C to stop")
            sync(source, replica, logfile)
            sleep(frequency)
    except KeyboardInterrupt:
        print("Script Stopped")
        exit(0)

if __name__ == "__main__":
    main()