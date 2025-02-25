import argparse
import os
import sys
import time

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
        sys.exit(1)

    if os.path.exists(args.source):
        
        if os.path.exists(args.replica):
            
            return 0
        else:
            print("Replica folder does not exist, new folder will be created") #log this
            return 0
    else:
        print("Source folder does not exist")
        sys.exit(1)

    try:
        while true:
            print("Running the Script. Press Ctrl+C to stop")
            #run sync
            time.sleep(frequency)
    except KeyboardInterrupt:
        print("Script Stopped")
        sys.exit(0)


if __name__ == "__main__":
    main()