import argparse
import os
from sys import exit
from time import sleep
from datetime import datetime
from pathlib import Path
import filecmp
import shutil

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    final_message = timestamp + " - " + message + "\n"
    logfile.write(final_message)
    print(final_message)

def sync_additions(source_path, replica_path):
    for item in os.listdir(source_path):
        sourceEntry = os.path.join(source_path, item)
        replicaEntry = os.path.join(replica_path, item)

        if os.path.isdir(sourceEntry):
            if  not os.path.exists(replicaEntry):
                log("Creating " + item + " at " + replica_path)
                os.makedirs(replicaEntry)
                sync_additions(sourceEntry, replicaEntry)
        else:
            if not os.path.exists(replicaEntry) or not filecmp.cmp(sourceEntry, replicaEntry):
                log("Copying " + item + " into " + replica_path)
                shutil.copy2(sourceEntry, replicaEntry) #copy2 attempts to perserve metadata

def sync_deletions(source_path, replica_path):
    for item in os.listdir(replica_path):
        sourceEntry = os.path.join(source_path, item)
        replicaEntry = os.path.join(replica_path, item)

        if not os.path.exists(sourceEntry):
            if os.path.isdir(sourceEntry):
                log("Deleting Folder " + item + " from " + replica_path)
                shutil.rmtree(replicaEntry)
            else:
                log("Deleting File " + item + " from " + replica_path)
                os.remove(replicaEntry)

def sync(source_path, replica_path):
    log("Beggining Synchonization by adding new content to replica folder")
    sync_additions(source_path, replica_path)
    log("Finished adding new content to replica folder")
    log("Cleaning deleted source files from replica folder")
    sync_deletions(source_path, replica_path)
    log("Finished cleaning deleted content from replica folder")
    log("Finished Synchonization")
    

def main():
    parser = argparse.ArgumentParser(description="Replicates a source folder frequently")
    parser.add_argument("-s", "--source", help="Path of the folder to be replicated", required=True)
    parser.add_argument("-r", "--replica", help="Path of the replica folder", required=True)
    parser.add_argument("-l", "--log", help="Path of the log file", required=True)
    parser.add_argument("-f", "--frequency", help="frequency with witch the replication must occur", required=True)
    args = parser.parse_args()

    source = args.source
    replica = args.replica
    frequency = args.frequency

    try:
        frequency = int(frequency)
    except ValueError:
        print("Invalid Frequency (Must be a numeric value)")
        exit(1)

    if os.path.exists(source):
        source = args.source
        if os.path.exists(replica):
            replica = args.replica
    else:
        print("Source folder does not exist")
        exit(1)

    if os.path.isfile(args.log):
        global logfile 
        logfile_path = Path(args.log)
        logfile = open(logfile_path,'w')
    else:
        print("Log file given is not valid")
        exit(1)

    try:
        while True:
            print("Running the Script. Press Ctrl+C to stop")
            sync(source, replica)
            sleep(frequency)
    except KeyboardInterrupt:
        print("Script Stopped")
        logfile.close()
        exit(0)

if __name__ == "__main__":
    main()