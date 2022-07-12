import socket
from flask import Flask

hostname = socket.gethostname()
ipaddress = socket.gethostbyname(hostname)
app = Flask(__name__)
@app.route("/")
def ip_and_port_preview():
    return f'''<html>
    <head>
        <title>IP & Port</title>
    </head>
    <body>
        <h1>Your IP is : <div id="ip">{ipaddress}</div></h1>
    </body>
</html>'''
