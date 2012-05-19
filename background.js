
function log(data) {
    console.log(data);
}

var udp_socket_writer = function(host, port, string) {
    var string2ArrayBufferAndWrite = function(str) {  // http://goo.gl/1eJnn
        var bb = new WebKitBlobBuilder();
        bb.append(str);
        var f = new FileReader();
        f.onload = function(e) {
            var data = e.target.result;
            chrome.experimental.socket.create(
                'udp', {},
                function(socketInfo) {
                    chrome.experimental.socket.connect(
                        socketInfo.socketId, host, port,
                        function(result) {
                            chrome.experimental.socket.write(socketInfo.socketId, data,
                                                             function(writeInfo){ console.log(writeInfo); })
                        });
                });
        };
        f.readAsArrayBuffer(bb.getBlob());
    };
    string2ArrayBufferAndWrite(string);
}
