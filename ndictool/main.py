# Author: Patrick Blanchard
# Contact: pblanc5@lsu.edu --or-- patrickblanchard.dev@gmail.com
# Description: Entry point of project
#
##################################################################
# Change Log
##################################################################
# 08-29-17: pblanc5 "Add read_yaml and main"
# 08-31-17: pblanc5 "Add iosinterface"
# 09-06-17: pblanc5 "iosinterface -> ios_interface"

import getpass
import ios_interface
import yaml
import sys


# Reads yaml file used for configuration
def read_yaml(conf_file):
    try:
        with open(conf_file) as f:
            return yaml.load(f)
    except Exception as inst:
        print inst
        exit(1)

def main():
    USER = raw_input("Enter Username: ")
    PASS = getpass.getpass("Enter Password: ")
    CONF = {}

    if len(sys.argv) > 0:
        CONF = read_yaml(sys.argv[1])
    else:
        print "Please specify a configuration file."
        sys.exit(1)

    console_server = CONF["console_server"]
    domain_name = CONF["domain_name"]
    ios_interface_list = CONF["ios_interface"]

    for interface in ios_interface_list:
        IOS_INT = ios_interface.IOSInterface(console_server, interface, domain_name)
        print IOS_INT
        IOS_INT.update(USER, PASS)

if __name__ == "__main__":
    main()
