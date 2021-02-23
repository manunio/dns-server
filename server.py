# import dnspython as dns
# import dns.resolver

# result = dns.resolver.resolve('google.com', 'A')
# for ipval in result:
#     print('IP', ipval.to_text())

from dnslib.server import DNSServer, DNSLogger
from dnslib.dns import RR


class TestResolver:
    def resolve(self, request, handler):
        reply = request.reply()
        reply.add_answer(*RR.fromZone("abc.def. 60 A 1.2.3.4"))
        return reply


resolver = TestResolver()

logger = DNSLogger(prefix=False)

server = DNSServer(resolver, port=8053, address="localhost", logger=logger, tcp=True)

server.start_thread()

try:
    while True:
        pass
except KeyboardInterrupt:
    server.stop()
