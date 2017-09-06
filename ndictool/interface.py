# Author: Patrick Blanchard
# Contact: pblanc5@lsu.edu --or-- patrickblanchard.dev@gmail.com
# Description: Base class for interface communication handling
#
##################################################################
# Change Log
##################################################################
# 09-06-17: pblanc5 "Create interface"

import paramiko
import time
import sys

class Interface():

    def __init__(self, host, port, domain):
        self.host = host
        self.port = port
        self.domain = domain
        self.client = paramiko.SSHClient()

    def __str__(self):
        return self.host + "\n" + str(self.port) + "\n" + self.domain

    def connect(self, user, passwd):
        # Establishes connection with switch and emulates teminal session

        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        self.client.connect(hostname=self.host, port=(3000 + self.port), username=user, password=passwd)
        return self.client.invoke_shell()

    def destroy_connection(self):
        self.client.close()
