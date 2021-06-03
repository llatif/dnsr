from dns.resolver import dns

nameservers = ['172.16.0.1', '172.16.0.2']

resolver = dns.resolver.Resolver()
for ns in nameservers:
  
  resolver.nameservers = [ns]
  result = resolver.resolve('fred.lon.bnew.org', 'A')
    
  for ipval in result:
      print('Nameserver', result.nameserver, '\nIP', ipval.to_text())