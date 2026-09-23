# 🌐 Network Connection Sentinel

A lightweight Python security tool for monitoring network connections and identifying unusual connection activity.

## 🛡️ Overview

Network Connection Sentinel monitors active network connections on a Windows system and records connection activity.

The tool maintains a local activity log and assigns a basic risk level based on the number of active network connections.

## ✨ Features

- 🌐 Network connection monitoring
- 🔄 Active connection detection
- 📝 Local security event logging
- 📊 Basic activity-based risk classification
- 🕒 Timestamped security events
- 💻 Lightweight command-line interface
- ⚡ Real-time monitoring with periodic checks

## 🔍 How It Works

Network Connection Sentinel continuously checks the active network connections on the system.

When a new connection is detected, the tool:

1. Detects the active network connection
2. Records the connection event
3. Captures the timestamp
4. Identifies the connection details
5. Calculates a basic risk level
6. Displays the security event

When a connection disappears, the disconnection is also recorded.

## 🚦 Risk Classification

| Risk Level | Condition |
|---|---|
| 🟢 LOW | Fewer than 10 active connections |
| 🟡 MEDIUM | 10–19 active connections |
| 🔴 HIGH | 20 or more active connections |

> The risk level is a simple activity-based indicator and does not determine whether a network connection is malicious.

## 🗂️ Activity Logging

Security events are stored locally in:

    network_activity.log

Each event contains:

### 🕒 Timestamp

Records the exact date and time when the network event occurred.

### 🔄 Event Type

Identifies whether the network connection was detected or disconnected.

### 🌐 Network Connection

Records the detected local and remote connection information.

### 🔌 Protocol

Records the network protocol associated with the connection, such as TCP or UDP.

## 🧰 Technologies Used

### 🐍 Python

Core programming language used to build the network monitoring tool.

### 💻 Operating System Interface (`os`)

Used for interacting with the operating system and supporting system-level monitoring operations.

### 🌐 Socket (`socket`)

Used to work with network-related information such as IP addresses and host details.

### 📦 JSON (`json`)

Used to structure security event data before storing it in the log.

### 🕒 Date and Time (`datetime`)

Used to generate timestamps for network security events.

### ⏱️ Time-based Monitoring (`time`)

Used to periodically check for changes in active network connections.

## 🚀 How to Run

### 1. Clone the Repository

    git clone https://github.com/nithyashree-24/Network-Connection-Sentinel.git

### 2. Open the Project Folder

    cd Network-Connection-Sentinel

### 3. Run the Program

    python network_sentinel.py

   ## 🎯 Project Objective

The objective of Network Connection Sentinel is to demonstrate a simple network-security monitoring concept using Python.The project focuses on detecting network connection activity, recording security events, and presenting basic risk indicators that can be extended into a more advanced network monitoring system.
 
## 🔮 Future Enhancements

### 🔹 Process Identification

Identify which application or process is responsible for each network connection.

### 🔹 Remote Address Analysis

Analyze remote IP addresses and identify potentially suspicious destinations.

### 🔹 Trusted Connection Management

Maintain a list of trusted IP addresses, ports, and applications and flag unknown connections.

### 🔹 Advanced Risk Scoring

Combine connection frequency, remote addresses, ports, protocols, and process information into a more detailed risk score.

### 🔹 Security Dashboard

Build a graphical dashboard for viewing network events, risk levels, active connections, and historical activity.

## ⚠️ Security Note

Network Connection Sentinel is intended for educational and defensive security monitoring purposes.

The risk classification is a basic indicator and should not be treated as a definitive determination of malicious network activity.
