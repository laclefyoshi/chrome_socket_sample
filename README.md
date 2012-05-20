
chrome_socket_sample
====================

Introduction
------------

This is an extension using `chrome.experimental.socket.*`.

Usage
-----

Install on Google Chrome Canary build
<https://tools.google.com/dlpage/chromesxs>. Allow using experimental
API on settings page.

Open popup of this extension. Input host, port of a server running
`udpserver.py` and message and send.

If you want to use `chrome.experimental.*` API directly, open Inspect
views of `background.html` of this extension with Developer tools.
