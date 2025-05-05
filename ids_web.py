from flask import Flask, jsonify, render_template
from scapy.all import sniff, TCP, IP
import threading

app = Flask(__name__)
alerts = []

# Détection de scan
def detect_scan(pkt):
    if pkt.haslayer(TCP) and pkt.haslayer(IP):
        port = pkt[TCP].dport
        ip = pkt[IP].src
        alert = f"Scan détecté : {ip} vers port {port}"
        print(alert)
        alerts.append(alert)

# Thread de sniff non-bloquant
def start_sniff():
    sniff(filter="tcp", prn=detect_scan, store=0)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/alerts")
def get_alerts():
    return jsonify(alerts[-10:])  # les 10 dernières alertes

if __name__ == "__main__":
    thread = threading.Thread(target=start_sniff, daemon=True)  # daemon=True pour ne pas bloquer
    thread.start()
    app.run(debug=True)
