from flask import Flask ,jsonify , render_template
import socket
app = Flask(__name__)

#Function to fetch hostname and ip details
def fetchDetails():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    return host_name,host_ip

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"   

@app.route("/health")
def health():
    return jsonify(   # will jsonify the response 
        status = "UP"        
    )
@app.route("/details")
def details():
    hostname,ip = fetchDetails() # open a tuple 
    return render_template('index.html',HOSTNAME = hostname, IP = ip) # passed the hostname and ip to index.html .


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
