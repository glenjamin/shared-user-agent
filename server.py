import sys
import webbrowser
from SocketServer import TCPServer, StreamRequestHandler

try:
    port = int(sys.argv[1])
except:
    print "Using default port: 6688"
    port = 6688

class OpenBrowser(StreamRequestHandler):
    def handle(self):
        url = self.rfile.readline().strip()
        print "Opening %s" % url
        webbrowser.open(url)
        self.wfile.write("success")

if __name__ == '__main__':
    server = TCPServer(("", port), OpenBrowser)
    server.serve_forever()
