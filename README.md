# Python Port Scanner

A multithreaded TCP Port Scanner built using Python. This project scans a target IP address for open TCP ports and displays the associated service names.

## Features

* Multithreaded scanning for faster results
* Detects open TCP ports
* Displays common service names (HTTP, SSH, FTP, etc.)
* Measures total scan time
* Uses Python sockets for network communication

## Technologies Used

* Python 3
* socket
* concurrent.futures (ThreadPoolExecutor)
* time

## How to Run

1. Clone this repository.
2. Run the Python script.
3. Enter the target IP address.
4. View the list of open ports and their services.

## Example

Target IP: 45.33.32.156

Open Ports:

* 22 — SSH
* 80 — HTTP

## Disclaimer

This tool is intended for educational purposes and authorized security testing only. Only scan systems you own or have explicit permission to test.
