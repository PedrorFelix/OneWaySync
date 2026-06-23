import argparse
import os
from sys import exit
from time import sleep
from datetime import datetime
from pathlib import Path
import filecmp
import shutil

def log(message, logfile):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    final_message = timestamp + " - " + message + "\n"
    logfile.write(final_message)
    print(final_message)

def sync_additions(source_path, replica_path, logfile):
    for item in os.listdir(source_path):
        sourceEntry = os.path.join(source_path, item)
        replicaEntry = os.path.join(replica_path, item)

        if os.path.isdir(sourceEntry):
            if  not os.path.exists(replicaEntry):
                log("ACTION - Creating " + item + " at " + replica_path + ".", logfile)
                os.makedirs(replicaEntry)
            sync_additions(sourceEntry, replicaEntry, logfile)
        else:
            if not os.path.exists(replicaEntry):
                log("ACTION - Copying " + item + " into " + replica_path + ".", logfile)
                shutil.copy2(sourceEntry, replicaEntry) #copy2 attempts to preserve metadata
            elif not filecmp.cmp(sourceEntry, replicaEntry, shallow=False):
                log("ACTION - Updating " + item + " into " + replica_path + ".", logfile)
                shutil.copy2(sourceEntry, replicaEntry)

def sync_deletions(source_path, replica_path, logfile):
    for item in os.listdir(replica_path):
        sourceEntry = os.path.join(source_path, item)
        replicaEntry = os.path.join(replica_path, item)

        if not os.path.exists(sourceEntry):
            if os.path.isdir(replicaEntry):
                log("ACTION - Deleting Folder " + item + " from " + replica_path + ".", logfile)
                shutil.rmtree(replicaEntry)
            else:
                log("ACTION - Deleting File " + item + " from " + replica_path + ".", logfile)
                os.remove(replicaEntry)

def sync(source_path, replica_path, logfile):
    log("INFO - Synchronization Started.", logfile)
    sync_additions(source_path, replica_path, logfile)
    log("INFO - New content added to replica folder.", logfile)
    log("INFO - Cleaning replica folder from removed content.", logfile)
    sync_deletions(source_path, replica_path, logfile)
    log("INFO - Cleaning finished.", logfile)
    log("INFO - Synchronization Finished, waiting for next run.", logfile)
    

def main():
    parser = argparse.ArgumentParser(description="Replicates a source folder frequently")
    parser.add_argument("-s", "--source", help="Path of the folder to be replicated", required=True)
    parser.add_argument("-r", "--replica", help="Path of the replica folder", required=True)
    parser.add_argument("-l", "--log", help="Path of the log file", required=True)
    parser.add_argument("-f", "--frequency", help="frequency with which the replication must occur", required=True)
    args = parser.parse_args()

    source = args.source
    replica = args.replica
    frequency = args.frequency

    try:
        frequency = int(frequency)
    except ValueError:
        print("Invalid Frequency (Must be a numeric value).")
        exit(1)

    if not os.path.exists(source):
        print("Source folder does not exist.")
        exit(1)
    if not os.path.exists(replica):
        print("Replica folder not found, creating new folder.")
        os.makedirs(replica)

    logfile_path = Path(args.log)
    if not logfile_path.parent.exists():
        print("Log file path is not valid, directory does not exist.")
        exit(1)

    try:
        while True:
            print("Running the Script. Press Ctrl+C to stop.")
            with open(logfile_path, 'a') as logfile:
                sync(source, replica, logfile)
            sleep(frequency)
    except KeyboardInterrupt:
        print("Script Stopped.")
        exit(0)

if __name__ == "__main__":
    main()