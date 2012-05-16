#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright : (c) SAEKI Yoshiyasu
# License   : MIT-style license
#             <http://www.opensource.org/licenses/mit-license.php>
# last updated: 2012/05/15

import socket

if __name__ == "__main__":
    udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpsock.bind(("", 9998))
    while True:
        data, addr = udpsock.recvfrom(1024)
        print "%s wrote: %s" % (addr, data)

