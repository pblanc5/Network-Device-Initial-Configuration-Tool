# Author: Patrick Blanchard
# Contact: pblanc5@lsu.edu --or-- patrickblanchard.dev@gmail.com
# Description: Sends IOS commands to specified switches
#
##################################################################
# Change Log
##################################################################
# 08-31-17: pblanc5 "Create iosinterface"

import paramiko
import time
import sys

class IOSInterface():

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

    def enable(self, conn):
        conn.send('\r\n\r\n')
        prompt = conn.recv(1024)
        while True:
            if '#' in prompt:
                print "enabled"
                break
            elif '>' in prompt:
                conn.send('enable\n')
                print "enabling"
                break
            else:
                conn.send('\r\n\r\n')
                time.sleep(1)
                prompt = conn.recv(1024)
                print "spinning"

    def configure_interfaces(self, conn):
        # Sends interface configuration

        conn.send('\r\n\r\n')
        conn.send('\r\n\r\n')
        time.sleep(1)
        conn.send('configure terminal\n')
        time.sleep(1)
        conn.send('interface vlan 1\n')
        conn.send('ip address 10.0.0.' + str(self.port) + ' 255.255.255.0\n')
        conn.send('exit\n')
        time.sleep(1)
        conn.send('interface Gi 1/0/1\n')
        conn.send('no shutdown\n')
        conn.send('exit\n')
        print conn.recv(5000)
        time.sleep(2)


    def configure_ssh(self, conn):
        # configure ssh settings

        conn.send('\r\n\r\n')
        conn.send('configure terminal\n')
        conn.send('hostname switch-' + str(self.port) + '\n')
        conn.send('ip domain-name ' + self.domain + '\n')
        conn.send('crypto key generate rsa modulus 1024\n')
        time.sleep(3)
        conn.send('aaa new-model\n')
        conn.send('username admin priv 15 secret password\n')
        conn.send('line vty 0 15\n')
        conn.send('transport input ssh\n')
        conn.send('exit\nexit\n')
        print conn.recv(5000)
        time.sleep(2)

    def destroy_connection(self):
        self.client.close()

    def update(self, user, passwd):
        try:
            conn = self.connect(user, passwd)
            self.enable(conn)
            self.configure_interfaces(conn)
            self.configure_ssh(conn)
            self.destroy_connection()
        except Exception as error:
            print error
        finally:
            if self.client:
                self.client.close()
