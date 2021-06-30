#!/usr/bin/env python3
#


#################################################################
#                                                               #
#                                                               #
#                                                               #
#                                                               #
#       ██████╗  ██████╗  ██████╗ ██████╗ ██╗███╗   ██╗██╗      #
#       ██╔░░██╗██╔░████╗██╔░████╗██╔░░██╗██║████╗  ██║██║      #
#       ██████╔╝██║██╔██║██║██╔██║██████╔╝██║██╔██╗ ██║██║      #
#       ██╔░░██╗████╔╝██║████╔╝██║██╔░░██╗██║██║╚██╗██║██║      #
#       ██║  ██║╚██████╔╝╚██████╔╝██████╔╝██║██║ ╚████║██║      #
#       ╚░╝  ╚░╝ ╚░░░░░╝  ╚░░░░░╝ ╚░░░░░╝ ╚░╝╚░╝  ╚░░░╝╚░╝      #
#                                                               #
#              Email    : roobini.gamer@protonmail.com          #
#              Instagram: https://bit.ly/3iX0ljO                #
#              Youtube  : https://bit.ly/2Emapnn                #
#              Facebook : https://bit.ly/3he568k                #
#              Github   : https://bit.ly/2E8gFzx                #
#                                                               #
#################################################################

### Banner ####

__author__ = "R00B!Ni"
__copyright__ = "roobini-gamer.blogspot.com"
__version__ = "0.1b"
__license__ = "GPL 3.0"


import sys
from os import devnull, environ
from os.path import basename, isfile
from random import randint
from socket import gethostname
from subprocess import call, getoutput
from sys import exit, stderr, stdout
from time import asctime, sleep

sys.tracebacklimit = 0
fnull = open(devnull, 'w')


class Colors:
  Escape = "\033"
  Lred = "[91m"
  Lgre = "[92m"
  Lyel = "[93m"


class Header:
  headers = {
      1:
          r"""
        ▒███████▒ ▄▄▄       █     █░ ▄▄▄       ██▀███   █    ██ ▓█████▄  ▒█████  
        ▒ ▒ ▒ ▄▀░▒████▄    ▓█░ █ ░█░▒████▄    ▓██ ▒ ██▒ ██  ▓██▒▒██▀ ██▌▒██▒  ██▒
        ░ ▒ ▄▀▒░ ▒██  ▀█▄  ▒█░ █ ░█ ▒██  ▀█▄  ▓██ ░▄█ ▒▓██  ▒██░░██   █▌▒██░  ██▒
          ▄▀▒   ░░██▄▄▄▄██ ░█░ █ ░█ ░██▄▄▄▄██ ▒██▀▀█▄  ▓▓█  ░██░░▓█▄   ▌▒██   ██░
        ▒███████▒ ▓█   ▓██▒░░██▒██▓  ▓█   ▓██▒░██▓ ▒██▒▒▒█████▓ ░▒████▓ ░ ████▓▒░
        ░▒▒ ▓░▒░▒ ▒▒   ▓▒█░░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ 
        ░░▒ ▒ ░ ▒  ▒   ▒▒ ░  ▒ ░ ░    ▒   ▒▒ ░  ░▒ ░ ▒░░░▒░ ░ ░  ░ ▒  ▒   ░ ▒ ▒░ 
        ░ ░ ░ ░ ░  ░   ▒     ░   ░    ░   ▒     ░░   ░  ░░░ ░ ░  ░ ░  ░ ░ ░ ░ ▒  
          ░ ░          ░  ░    ░          ░  ░   ░        ░        ░        ░ ░  
          ░                                                        ░           0.1b
                        ZA-WARUDO framwork MADE By R00B!Ni_gamer                  
	                       
	                    www.roobini-gamer.blogspot.com""",
      2:
      
          r"""
         ▄███████▄     ▄████████  ▄█     █▄     ▄████████    ▄████████ ███    █▄  ████████▄   ▄██████▄  
        ██▀     ▄██   ███    ███ ███     ███   ███    ███   ███    ███ ███    ███ ███   ▀███ ███    ███   
              ▄███▀   ███    ███ ███     ███   ███    ███   ███    ███ ███    ███ ███    ███ ███    ███ 
         ▀█▀▄███▀▄▄   ███    ███ ███     ███   ███    ███  ▄███▄▄▄▄██▀ ███    ███ ███    ███ ███    ███    
          ▄███▀   ▀ ▀███████████ ███     ███ ▀███████████ ▀▀███▀▀▀▀▀   ███    ███ ███    ███ ███    ███ 
        ▄███▀         ███    ███ ███     ███   ███    ███ ▀███████████ ███    ███ ███    ███ ███    ███ 
        ███▄     ▄█   ███    ███ ███ ▄█▄ ███   ███    ███   ███    ███ ███    ███ ███   ▄███ ███    ███ 
         ▀████████▀   ███    █▀   ▀███▀███▀    ███    █▀    ███    ███ ████████▀  ████████▀   ▀██████▀  
                                                             ███    ███                          0.1b    

                                     ZA-WARUDO framwork MADE By R00B!Ni_gamer                  
	                       
                                         www.roobini-gamer.blogspot.com""",
      3:
          r"""
        ·▄▄▄▄• ▄▄▄· ▄▄▌ ▐ ▄▌ ▄▄▄· ▄▄▄  ▄• ▄▌·▄▄▄▄        
        ▪▀·.█▌▐█ ▀█ ██· █▌▐█▐█ ▀█ ▀▄ █·█▪██▌██▪ ██ ▪     
        ▄█▀▀▀•▄█▀▀█ ██▪▐█▐▐▌▄█▀▀█ ▐▀▀▄ █▌▐█▌▐█· ▐█▌ ▄█▀▄ 
        █▌▪▄█▀▐█ ▪▐▌▐█▌██▐█▌▐█ ▪▐▌▐█•█▌▐█▄█▌██. ██ ▐█▌.▐▌
        ·▀▀▀ • ▀  ▀  ▀▀▀▀ ▀▪ ▀  ▀ .▀  ▀ ▀▀▀ ▀▀▀▀▀•  ▀█▄▀▪  
                                                      0.1b
           ZA-WARUDO framwork MADE By R00B!Ni_gamer                  
	                      
              www.roobini-gamer.blogspot.com""",
      4:
          r"""
        ███████╗ █████╗       ██╗    ██╗ █████╗ ██████╗ ██╗   ██╗██████╗  ██████╗ 
        ╚══███╔╝██╔══██╗      ██║    ██║██╔══██╗██╔══██╗██║   ██║██╔══██╗██╔═══██╗
          ███╔╝ ███████║█████╗██║ █╗ ██║███████║██████╔╝██║   ██║██║  ██║██║   ██║
         ███╔╝  ██╔══██║╚════╝██║███╗██║██╔══██║██╔══██╗██║   ██║██║  ██║██║   ██║
        ███████╗██║  ██║      ╚███╔███╔╝██║  ██║██║  ██║╚██████╔╝██████╔╝╚██████╔╝
        ╚══════╝╚═╝  ╚═╝       ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝ 
                                                                               0.1b
                      ZA-WARUDO framwork MADE By R00B!Ni_gamer                  
                      
	                 www.roobini-gamer.blogspot.com""",
  }

### Tools Used ####

class Tools:
  tool = {
      'helper': 'which',
      3: "wifite",
      4: "gvm-setup",
      5: "veil",
      6: "websploit",
      7: "msfdb",
      8: "setoolkit"
  }

### Anonesurf (part1) ####


class TorIptables:

  def __init__(self):
    self.local_dnsport = "53"  ## DNS Port
    self.virtual_net = "10.0.0.0/10"  ## Virtual Network
    self.local_loopback = "127.0.0.1"  ## The Local Loopback
    self.non_tor_net = ["192.168.0.0/16", "172.16.0.0/12"] ## Non Tor Network
    self.non_tor = ["127.0.0.0/9", "127.128.0.0/10", "127.0.0.0/8"] ## Non Tor 
    self.tor_uid = getoutput("id -ur debian-tor") ## Tor User UID
    self.trans_port = "9040" ## Tor Port
    self.tor_config_file = '/etc/tor/torrc' ## Tor Config
    self.torrc = r'''


VirtualAddrNetwork %s ## Inserted by %s for tor iptables rules set
AutomapHostsOnResolve 1
TransPort %s ## Transparently route all traffic thru tor on port %s
DNSPort %s
''' % (basename(__file__), self.trans_port, self.virtual_net, self.trans_port,
       self.local_dnsport)

  @staticmethod
  def get_public_ip():
    return ''.join(getoutput('curl -4s ipinfo.io/ip').split()[-1:])

  def flush_iptables_rules(self):
    call(["iptables", "-F"])
    call(["iptables", "-t", "nat", "-F"])

  def load_iptables_rules(self):
    self.flush_iptables_rules()
    if self.non_tor_net[0] not in self.non_tor:
      self.non_tor.extend(self.non_tor_net)
    
    ## Call The Local Loopback 1
    call([ 
        "iptables", "-I", "OUTPUT", "!", "-o", "lo", "!", "-d",
        self.local_loopback, "!", "-s", self.local_loopback, "-p", "tcp", "-m",
        "tcp", "--tcp-flags", "ACK,FIN", "ACK,FIN", "-j", "DROP"
    ])
    ## Call The Local Loopback 2
    call([
        "iptables", "-I", "OUTPUT", "!", "-o", "lo", "!", "-d",
        self.local_loopback, "!", "-s", self.local_loopback, "-p", "tcp", "-m",
        "tcp", "--tcp-flags", "ACK,RST", "ACK,RST", "-j", "DROP"
    ])

    ## Call Tor User UID
    call([
        "iptables", "-t", "nat", "-A", "OUTPUT", "-m", "owner", "--uid-owner",
        "%s" % self.tor_uid, "-j", "RETURN"
    ])

    ## Call DNS Port
    call([
        "iptables", "-t", "nat", "-A", "OUTPUT", "-p", "udp", "--dport",
        self.local_dnsport, "-j", "REDIRECT", "--to-ports", self.local_dnsport
    ])

    ## Call Non Tor
    for net in self.non_tor:
      call([
          "iptables", "-t", "nat", "-A", "OUTPUT", "-d", "%s" % net, "-j", "RETURN"
      ])

    call([
        "iptables", "-t", "nat", "-A", "OUTPUT", "-p", "tcp", "--syn", "-j",
        "REDIRECT", "--to-ports", "%s" % self.trans_port
    ])

    call([
        "iptables", "-A", "OUTPUT", "-m", "state", "--state",
        "ESTABLISHED,RELATED", "-j", "ACCEPT"
    ])

    ## Call Non Tor
    for net in self.non_tor:
      call(["iptables", "-A", "OUTPUT", "-d", "%s" % net, "-j", "ACCEPT"])

    ## Tor User UID
    call([
        "iptables", "-A", "OUTPUT", "-m", "owner", "--uid-owner",
        "%s" % self.tor_uid, "-j", "ACCEPT"
    ])
    call(["iptables", "-A", "OUTPUT", "-j", "REJECT"])

    ## Restart Tor
    call(["service", "tor", "restart"], stdout=fnull, stderr=fnull)




### Main Menu ###

def main_menu():
  print("        {0}".format(
      c.Escape + c.Lyel +
      "[1]  [  Anonymizer ] [route all traffic thru Tor.                    ]\n"))
  print("        {0}".format(
      "[2]  [De-Anonymizer] [Flush Tor Iptables rules                       ]\n"))
  print("        {0}".format(
      "[3]  [    WiFite   ] [Automated wireless auditor, designed for Linux.]\n"))
  print("        {0}".format(
      "[4]  [   OpenVas   ] [Vulnerability scanning and management.         ]\n"))
  print("        {0}".format(
      "[5]  [ Veil-Evasion] [Generate metasploit payloads bypass anti-virus.]\n"))
  print("        {0}".format(
      "[6]  [  Websploit  ] [WebSploit Advanced MITM Framework.             ]\n"))
  print("        {0}".format(
      "[7]  [  Metasploit ] [Executing exploit code against target.         ]\n"))
  print("        {0}".format(
      "[8]  [     SET     ] [Social-Engineer Toolkit                        ]\n"))
  print("        {0}".format(c.Escape + c.Lred + "[9]  [Exit         ] [Exit The Script                                ]\n"))

### Anonymity State ###


def anon_status():
  anon = getoutput(
      "iptables -S -t nat | grep %s" % TorIptables().local_dnsport)
  if anon:
    print("        {0} {1}".format(
        "Anonymizer status", c.Escape + c.Lgre + "[ ON ] -=[ WAN IP: " +
        "%s ]=-\n" % (TorIptables.get_public_ip())))
  else:
    print("        {0} {1}".format(
        "Anonymizer status", c.Escape + c.Lred + "[ OFF ] -=[ LAN IP: " +
        "%s ]=-\n" % (getoutput('hostname -I').split()[0])))


### Anonesurf (part2) + menu input/exit ####


if __name__ == '__main__':
  load_tables = TorIptables()
  try:
    while True:
      call(['reset'])
      call(['clear'])
      try:
        c = Colors()
        print(c.Escape + "[" + repr(randint(92, 97)) + "m" +
              Header().headers[randint(1, 4)] + "\n\n")
        
        anon_status()
        main_menu()
        try:
          tool = Tools().tool
          selected = int(
              input(c.Escape + c.Lgre + gethostname() + "-ZaWarudo"
                       + ":> "))
          if selected < 1 or selected > 0:
            print("Select a number between 1 and 9")
            sleep(2)
          if selected == 9:
            exit(9)
          if selected == 1:
            if isfile(load_tables.tor_config_file):
              if not 'VirtualAddrNetwork' in open(
                  load_tables.tor_config_file).read():
                with open(load_tables.tor_config_file, 'a+') as torrconf:
                  torrconf.write(load_tables.torrc)
            load_tables.load_iptables_rules()
          sleep(1)

          if selected == 2:
            load_tables.flush_iptables_rules()
            sleep(1)
          if selected == 3:
            call(['clear'])
            call([getoutput(tool['helper'] + ' ' + tool[3])])
            sleep(1)
          if selected == 4:
            call(['clear'])
            call([getoutput(tool['helper'] + ' ' + tool[4])])
            sleep(1)
          if selected == 5:
            call(['clear'])
            call([getoutput(tool['helper'] + ' ' + tool[5])])
            sleep(1)
          if selected == 6:
            call(['clear'])
            call([getoutput(tool['helper'] + ' ' + tool[6])])
            sleep(1)
          if selected == 7:
            call(['clear'])
            call([getoutput(tool['helper'] + ' ' + tool[7]), 'run'])
            sleep(1)
          if selected == 8:
            call(['clear'])
            call([getoutput(tool['helper'] + ' ' + tool[8])])
            sleep(5)
        except ValueError:
          print("Select a number between 1 and 9")
          sleep(2)
      except SystemExit:
        exit(9)
  except OSError as err:
    print("\n [*] Check your path " + c.Escape + c.Lred + "%s\n %s" %
          (environ['PATH'], "[!] " + c.Escape + c.Lyel + "Can't find"),
          c.Escape + c.Lgre + tool[selected] + ",", 
          c.Escape + c.Lred + "Aborting!")
    sleep(2)
    pass


#################################################################
#                                                               #
#                                                               #
#                                                               #
#                                                               #
#       ██████╗  ██████╗  ██████╗ ██████╗ ██╗███╗   ██╗██╗      #
#       ██╔══██╗██╔═████╗██╔═████╗██╔══██╗██║████╗  ██║██║      #
#       ██████╔╝██║██╔██║██║██╔██║██████╔╝██║██╔██╗ ██║██║      #
#       ██╔══██╗████╔╝██║████╔╝██║██╔══██╗██║██║╚██╗██║██║      #
#       ██║  ██║╚██████╔╝╚██████╔╝██████╔╝██║██║ ╚████║██║      #
#       ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝╚═╝      #
#                                                               #
#              Email    : roobini.gamer@protonmail.com          #
#              Instagram: https://bit.ly/3iX0ljO                #
#              Youtube  : https://bit.ly/2Emapnn                #
#              Facebook : https://bit.ly/3he568k                #
#              Github   : https://bit.ly/2E8gFzx                #
#                                                               #
#################################################################