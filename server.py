"""
From http://www.huyng.com/posts/modifying-python-simplehttpserver/
"""

import os
import SocketServer
import SimpleHTTPServer
import urllib

PORT = int(os.environ['PORT'])
ADDRESS = os.environ['IP']

import os
import posixpath
import urllib
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# modify this to add additional routes
ROUTES = (
    # [url_prefix ,  directory_path]
    ['/media', '/var/www/media'],
    ['', os.path.join(PROJECT_ROOT, 'app-root/repo/site/output')]  # empty string for the 'default' match
)

class RequestHandler(SimpleHTTPRequestHandler):
    
    def translate_path(self, path):
        """translate path given routes"""

        # set default root to cwd
        root = os.getcwd()
        
        # look up routes and set root directory accordingly
        for pattern, rootdir in ROUTES:
            if path.startswith(pattern):
                # found match!
                path = path[len(pattern):]  # consume path up to pattern len
                root = rootdir
                break
        
        # normalize path and prepend root directory
        path = path.split('?',1)[0]
        path = path.split('#',1)[0]
        path = posixpath.normpath(urllib.unquote(path))
        words = path.split('/')
        words = filter(None, words)
        
        path = root
        for word in words:
            drive, word = os.path.splitdrive(word)
            head, word = os.path.split(word)
            if word in (os.curdir, os.pardir):
                continue
            path = os.path.join(path, word)

        return path

def test(HandlerClass, ServerClass, protocol="HTTP/1.0"):
    """Test the HTTP request handler class.

    This runs an HTTP server on port 8000 (or the first command line
    argument).
    """
    server_address = (ADDRESS, PORT)

    HandlerClass.protocol_version = protocol
    httpd = ServerClass(server_address, HandlerClass)

    sa = httpd.socket.getsockname()
    print "Serving HTTP on", server_address, "..."
    httpd.serve_forever()

if __name__ == '__main__':
    test(RequestHandler, BaseHTTPServer.HTTPServer)
