import socket
import sys
import webbrowser

url = " ".join(sys.argv[1:])

try:
    from settings import HOST, PORT

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    sock.send(data + "\n")
    received = sock.recv(1024)
    sock.close()

    print "Sent:     %s" % data
    print "Received: %s" % received
except Exception, ex:
    sys.stderr.write(str(ex))
    webbrowser.open(url)
