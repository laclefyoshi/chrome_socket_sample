#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright : (c) SAEKI Yoshiyasu
# License   : MIT-style license
#             <http://www.opensource.org/licenses/mit-license.php>
# last updated: 2012/05/20

import SocketServer


class TCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print "%s wrote: " % self.client_address[0],
        print "%s" % self.data
        self.request.send("You wrote: %s" % self.data)

if __name__ == "__main__":
    server = SocketServer.TCPServer(("localhost", 9998), TCPHandler)
    server.serve_forever()
