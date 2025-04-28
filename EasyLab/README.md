# CVE-2017-18342 PyYAML Exploitation Lab

## 🧪 Overview
This lab demonstrates CVE-2017-18342: arbitrary code execution through unsafe `yaml.load()`.

## 🛠️ Setup Instructions

### Prerequisites
- Docker Desktop installed
- Python 3 installed
- PowerShell

### 1. Build and Run the Vulnerable Container
```powershell
cd EasyLab
docker build -t vuln-server .
docker run -d -p 5000:5000 --name vuln-container vuln-server
```

### 2. Run the Exploit
```powershell
python exploit_script.py
```
- This should create a file `/tmp/hacked.txt` **inside** the container.

### 3. Fix (Remediate) the Vulnerability
```powershell
docker stop vuln-container
docker rm vuln-container
Copy-Item .\remediation_server.py .\vulnerable_server.py -Force
docker build -t vuln-server .
docker run -d -p 5000:5000 --name vuln-container vuln-server
```

### 4. Test Again
```powershell
python exploit_script.py
```
- This time, **no file should be created**, and the exploit should fail.

## 🧠 Notes
- `yaml.load` allows arbitrary code execution.
- `yaml.safe_load` safely parses YAML without dangerous object loading.

## 📚 References
- [PyYAML GitHub](https://github.com/yaml/pyyaml)
- [CVE-2017-18342](https://nvd.nist.gov/vuln/detail/CVE-2017-18342)
