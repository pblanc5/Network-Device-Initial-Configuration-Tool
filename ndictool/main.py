# Author: Patrick Blanchard
# Contact: pblanc5@lsu.edu --or-- patrickblanchard.dev@gmail.com
# Description: Entry point and command line interface of project
#
##################################################################
# Change Log
##################################################################
# 08-29-17: pblanc5 "Add read_yaml and main"

import getpass
import yaml
import sys

# Reads yaml file used for configuration
def read_yaml(conf_file):
    try:
        with open(conf_file) as f:
            return yaml.load(f)
    except Exception as inst:
        print type(inst)
        print inst.args
        print inst
        exit(1)

def main():
    USER = raw_input("Enter Username: ")
    PASS = getpass.getpass("Enter Password: ")

    if len(sys.argv) > 0:
        read_yaml(sys.argv[1])
    else:
        print "Please specify a configuration file."
        sys.exit(1)

if __name__ == "__main__":
    main()
