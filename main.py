import argparse

def main():
    parser = argparse.ArgumentParser(description="Replicates a source folder frequently")
    parser.add_argument("-s", "--source", help="Path of the folder to be replicated", required=True)
    parser.add_argument("-r", "--replica", help="Path of the replica folder", required=True)
    parser.add_argument("-l", "--log", help="Path of the log file", required=True)
    parser.add_argument("-f", "--frequency", help="frequency with witch the replication must occur", required=True)
    args = parser.parse_args()

    print(f"arguments:\nsource: {args.source},\nreplica: {args.replica},\nlog: {args.log},\nfrequency: {args.frequency}")
    return 0

if __name__ == "__main__":
    main()