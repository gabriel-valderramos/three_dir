import os
import yaml
import json
import argparse
from pprint import pprint


def parse_args():
    parser = argparse.ArgumentParser(description="List all files recursively and save them into json or yaml file")
    parser.add_argument("--directory", "-d", help="The folder that you would like to list", required=True)
    parser.add_argument("--output", "-o", help="Where you would like to save the report")
    return parser.parse_args()


def parse_dir(args):
    raw_data = {}
    data = {}

    def set_data_by_path(keys, new_data):
        if not data.get(keys[0]):
            data[keys[0]] = {}
        
        tmp_data = data
        while keys:
            key = keys[0]
            last_item = True if len(keys) <= 1 else False

            if isinstance(tmp_data, dict):
                if not tmp_data.get(key):
                    tmp_data[key] = {}

                if last_item:
                    tmp_data[key]["files"] = new_data

                tmp_data = tmp_data[key]

            keys.pop(0)
        
        return data

    # creating raw data
    for directory, dirname, filenames in os.walk(args.directory):
        d = directory.replace("\\", "/")
        files = ["%s/%s" % (d, f) for f in filenames]

        raw_data[d] = files

    # fixing data
    for dir_name, files in raw_data.items():
        splited_dir = dir_name.split("/")
        set_data_by_path(splited_dir, files)

    if args.output:
        # save them on json file
        ext = args.output.split(".")[-1]
        assert ext in ["yaml", "yml", "json"], "Only json and yaml format are alowed"
        lib = yaml if ext in ["yaml", "yml"] else json
        with open(args.output, "w") as jf:
            lib.dump(data, jf, indent=2, sort_keys=True)
    else:
        pprint(data)


if __name__ == "__main__":
    args = parse_args()
    parse_dir(args)
