import time
import datetime
import argparse


starting_time = time.time()
version = "1.0.0"
# The argument
parser = argparse.ArgumentParser(prog='main')
parser.add_argument("--version", required=True,
                    help='Print the version of the code', action='store_true')

args = parser.parse_args()
if args.version:
    print(f"version: {version}")


endig_time = time.time()
time_diff = endig_time - starting_time

flag = True

while flag:
    print("{} Running for {:.2f} seconds".format(
        datetime.datetime.now(), time_diff))
    time.sleep(5)
    time_diff += 5
