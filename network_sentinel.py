import socket
import json
import time
from datetime import datetime
LOG_FILE = "network_events.json"
CHECK_INTERVAL = 5
def get_connections():
    connections = []
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        connections.append({
            "timestamp": datetime.now().isoformat(),
            "hostname": hostname,
            "local_ip": local_ip,
            "event": "NETWORK CHECK"
        })
    except Exception as error:
        connections.append({
            "timestamp": datetime.now().isoformat(),
            "event": "ERROR",
            "message": str(error)
        })
    return connections
def save_events(events):
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as file:
            for event in events:
                file.write(json.dumps(event) + "\n")
    except Exception as error:
        print("Log error:", error)
def display_event(event):
    print("-" * 55)
    print("NETWORK SENTINEL")
    print("-" * 55)
    print("Time      :", event["timestamp"])
    print("Event     :", event["event"])
    if "hostname" in event:
        print("Hostname  :", event["hostname"])
        print("Local IP  :", event["local_ip"])
    if "message" in event:
        print("Message   :", event["message"])
print("=" * 55)
print("           NETWORK CONNECTION SENTINEL")
print("=" * 55)
print("Monitoring network activity...")
print("Press Ctrl+C to stop.\n")
try:
    while True:
        events = get_connections()
        for event in events:
            display_event(event)
        save_events(events)
