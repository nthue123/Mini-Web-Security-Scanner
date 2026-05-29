# Mini Web Security Scanner

A simple beginner-friendly web security scanner built with Python.

This project helps beginners learn:

* Web reconnaissance
* HTTP requests
* Security headers
* Basic web security concepts
* Python automation

---

# Features

* HTTPS detection
* Security header analysis
* Server information detection
* robots.txt detection
* Basic web enumeration
* Colored terminal output

---

# Technologies Used

* Python 3
* requests
* colorama

---

# Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/mini-web-scanner.git
```

Move into the project folder:

```bash
cd mini-web-scanner
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Usage

Run the scanner:

```bash
python scanner.py
```

Enter a target URL:

```txt
Enter target URL: https://example.com
```

---

# Example Output

```txt
==================================================
 MINI WEB SECURITY SCANNER
==================================================

Target: https://example.com

[+] Checking HTTPS...
[OK] HTTPS enabled

[+] Checking Security Headers...
[MISSING] Content-Security-Policy
[OK] X-Frame-Options

[+] Checking Server Information...
[INFO] Server: nginx

[+] Checking robots.txt...
[FOUND] robots.txt

Scan completed.
```

---

# Project Structure

```txt
mini-web-scanner/
│
├── scanner.py
├── requirements.txt
└── README.md
```

---

# Security Checks

The scanner currently checks for:

* HTTPS usage
* Content-Security-Policy
* Strict-Transport-Security
* X-Frame-Options
* X-Content-Type-Options
* Referrer-Policy
* robots.txt exposure
* Server fingerprinting

---

# Future Improvements

Planned features:

* HTML report generation
* JSON export
* Multithreading
* Subdomain scanning
* Directory brute forcing
* Technology detection
* Basic vulnerability testing

---

# Learning Objectives

This project is designed to help beginners understand:

* HTTP requests and responses
* Web application security basics
* Security misconfiguration
* Reconnaissance techniques
* Python scripting for security

---

# Disclaimer

This tool is for educational purposes only.

Only scan:

* Your own systems
* Local labs
* CTF environments
* Authorized targets

Do not scan websites or systems without permission.


