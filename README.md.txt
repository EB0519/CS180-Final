CTF Lab: CVE Exploration & Live Demo
Objective
In this lab, you will investigate a real-world CVE (Common Vulnerabilities and Exposures), set up a vulnerable environment to demonstrate the exploitation of the vulnerability, and then apply remediation to fix the issue. The goal is to walk through the process of discovering, exploiting, and securing a system in a controlled, demonstrable way using Docker.

Lab Overview
CVE Selection: Choose a CVE from the provided list or search for a relevant CVE. The CVE chosen for this lab involves a Python vulnerability, which is exploited through insecure deserialization.

Vulnerability Understanding: Research the CVE to understand:

What the vulnerability is (e.g., insecure deserialization leading to remote code execution)

Why it occurs (e.g., improper handling of untrusted input in Python applications)

How it can be exploited (e.g., crafting malicious payloads that execute arbitrary code)

How it can be remediated (e.g., using secure deserialization methods like yaml.safe_load)

Lab Setup: Using Docker, we build and run a vulnerable Python server that can be exploited, followed by a fixed version that addresses the vulnerability.

Exploit and Remediation:

Exploit Script: A script demonstrating the vulnerable server being exploited.

Remediation Script: A fixed version of the server, demonstrating the security improvements.

Lab Requirements
To complete this lab, the following elements must be submitted:

Exploit Script: A working proof-of-concept showing the vulnerability in action.

Remediation Script: Code or configuration that fixes the vulnerability.

Dockerfile: Full build of the vulnerable environment.

README.md: Clear setup steps and how to run the exploit and remediation scripts.

Setup Instructions
1. Shut Down and Remove All Docker Containers
Before starting, ensure that all existing Docker containers are stopped and removed:

bash
Copy
Edit
sudo docker stop $(sudo docker ps -q)          # Stop all running containers
sudo docker rm $(sudo docker ps -a -q)         # Remove all containers (running and stopped)
2. Build the Vulnerable Docker Environment
To build the Docker image for the vulnerable server, use the following command:

bash
Copy
Edit
sudo docker build -f Dockerfile -t vulnerable-server .
Run the vulnerable container:

bash
Copy
Edit
sudo docker run -d -p 5000:5000 --name vulnerable-container vulnerable-server
3. Test the Vulnerability
Once the vulnerable container is running, navigate to the following URL in your browser:

arduino
Copy
Edit
http://localhost:5000/
You should see a page demonstrating the vulnerable server, which can be exploited.

4. Fix the Vulnerability
To fix the vulnerability, first find the current container ID:

bash
Copy
Edit
sudo docker ps -a
Then, remove the running vulnerable container:

bash
Copy
Edit
sudo docker rm -f {Current ID}
Next, build and run the fixed server container:

bash
Copy
Edit
sudo docker build -f DockerfileFixed -t fixed-server .
sudo docker run -d -p 5000:5000 --name fixed-container fixed-server
5. Test the Remediation
Once the fixed container is running, navigate to the following URL to verify that the vulnerability has been patched:

arduino
Copy
Edit
http://localhost:5000/
You should now see a more secure version of the application with the vulnerability fixed.

Exploitation and Remediation Scripts
Exploit Script: A Python script that demonstrates the vulnerability by sending a malicious payload to the vulnerable server.

Remediation Script: A Python script that remediates the vulnerability by securely deserializing the input data using yaml.safe_load.

Example Exploit Script
This script exploits insecure deserialization in the vulnerable server:

python
Copy
Edit
import requests

# Exploiting the vulnerability in the vulnerable server
url = 'http://localhost:5000/vulnerable_endpoint'
payload = {'data': 'malicious_payload'}
response = requests.post(url, data=payload)
print(response.text)
Example Remediation Script
This script demonstrates the remediation, using secure deserialization:

python
Copy
Edit
import yaml
from flask import Flask, request

app = Flask(__name__)

@app.route('/safe_endpoint', methods=['POST'])
def safe_endpoint():
    try:
        # Safely load YAML data
        data = yaml.safe_load(request.data)
        return f"Received data: {data}", 200
    except yaml.YAMLError as e:
        return f"Error processing data: {str(e)}", 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
Docker Setup
Dockerfile for Vulnerable Server
This Dockerfile sets up the vulnerable server environment:

Dockerfile
Copy
Edit
FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir Flask PyYAML

CMD ["python", "vulnerable_server.py"]
Dockerfile for Fixed Server
This Dockerfile sets up the fixed server environment:

Dockerfile
Copy
Edit
FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir Flask PyYAML

CMD ["python", "fixed_server.py"]
Submission Instructions
Ensure that all components of the lab are functioning properly, including:

Exploit script demonstrating the vulnerability

Remediation script fixing the vulnerability

Docker containers for both the vulnerable and fixed environments

Package the following files:

Exploit Script (exploit_script.py)

Remediation Script (remediation_server.py)

Vulnerable Dockerfile (Dockerfile)

Fixed Dockerfile (DockerfileFixed)

README.md (this file)

This README provides an overview of the setup, exploitation, and remediation process, ensuring that all elements of the lab are clearly documented and reproducible. Follow the instructions carefully to ensure that the lab is complete and meets all submission requirements.
