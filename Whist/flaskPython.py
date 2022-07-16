import socket
from flask import Flask

hostname = socket.gethostname()
ipaddress = socket.gethostbyname(hostname)
app = Flask(__name__)
@app.route("/")
def ip_preview():
    return f'''<html>
    <head>
        <title>IP Address</title>
    </head>
    <body>
        <h1>Your IP is : <div id="ip">{ipaddress}</div></h1>
    </body>
</html>'''


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
