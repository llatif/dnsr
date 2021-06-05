####
# dnsr - test DNS by querying a single host
# 
# Usage: /usr/bin/python3 dsnr [hostname]
####

import argparse
from dns.resolver import dns

parser = argparse.ArgumentParser()
parser.add_argument("host", help="A fully qualified hostname to test DNS")

## A list of name servers that we want to test
nameservers = ['172.16.0.1', '172.16.0.2']

def nsCheck(host):

  resolver = dns.resolver.Resolver()
  for ns in nameservers:

    ## Manually set the nameserver used to resolve queries from the list 
    resolver.nameservers = [ns]
    result = resolver.resolve(host, 'A')

    for ipval in result:
      ## TODO: send results to a database
      print('Nameserver', result.nameserver, '\nIP', ipval.to_text())

if __name__ == "__main__":

    # Parse command line arguments
    args = parser.parse_args() 
    
    nsCheck(args.host)