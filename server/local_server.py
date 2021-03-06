import SimpleHTTPServer
import SocketServer
import os
import threading

from EquirectangularViewer import config


try:
    from pydevd import *
except:
    None

server = None


def openWebApp(folder):
    SocketServer.TCPServer.allow_reuse_address = True
    global server
    if server is None:
        os.chdir(folder)
        server = SocketServer.TCPServer(
            ("", config.PORT), SimpleHTTPServer.SimpleHTTPRequestHandler)
        thread = threading.Thread(target=server.serve_forever)
        thread.daemon = True
        thread.start()


def shutdown():
    global server
    if server:
        server.shutdown()
        server = None
