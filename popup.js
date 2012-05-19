
var bg = chrome.extension.getBackgroundPage();

document.getElementById("button").onclick = function() {
    var host = document.getElementById("host").value;
    var port = parseInt(document.getElementById("port").value);
    var message = document.getElementById("message").value;
    bg.udp_socket_writer(host, port, message);
}
