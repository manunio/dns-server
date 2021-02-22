from pydnserver import DNSServer

ip = u'192.168.0.10  # Set this to the IP address of your network interface.

dns = DNSServer(interface=ip, port=53)
dns.start()

try:
    while True:
        pass

except KeyboardInterrupt:
    dns.stop()
